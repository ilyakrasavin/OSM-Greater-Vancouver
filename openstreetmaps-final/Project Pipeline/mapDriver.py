import pandas as pd
import numpy as np
import PIL
import folium
import sys
import os
import webbrowser

from utilHyp import haversineFunction, _convert_to_degress, getGPS

# MAP DRIVER AS FOUND IN A RECOMMENDATION NOTEBOOK

def plotmap(data, hints, move_mode, user_feed):

    # Load Recommendation relevant data.
    tourism = pd.read_json("./Prediction Data/tour_final")
    historic = pd.read_json("./Prediction Data/hist_final")
    food = pd.read_json("./Prediction Data/food_final")
    night = pd.read_json("./Prediction Data/night_final")
    subway = pd.read_json("./Prediction Data/subway_final")
    entertainment = pd.read_json("./Prediction Data/entr_final")
    
    map_full = folium.Map(
        location=[49.28, -123.12],
        zoom_start = 12
    )
    
    if move_mode == 'walk':
        threshold = 50
    elif move_mode == 'transit':
        threshold = 150
    elif move_mode == 'driving':
        threshold = 500
    
    # Find recommendation for each image on a path.
    for each in user_feed:

        folium.Marker([each[0], each[1]], popup = "YOU", icon = folium.Icon(color = 'green')).add_to(map_full)

        # Show closest subway stations if traveling by transit.
        if move_mode == 'transit' :
            subway_results = subway
            subway_results['distance'] = haversineFunction([subway_results['lat'], subway_results['lon']], each)
            subway_results = subway_results[subway_results['distance'] < 2500]
            subway_results = subway_results.iterrows()
            for idx, spot in subway_results:
                folium.Marker([spot['lat'], spot['lon']], popup = spot['name'], icon = folium.Icon(color = 'blue')).add_to(map_full)

        
        if data == 'tourism':
            # Recommend everything relevant from the category if no hints given.
            if(len(hints) == 0):
                results = tourism
                results['distance'] = haversineFunction([results['lat'], results['lon']], each)
                results = results[results['distance'] < threshold]
                results = results.iterrows()
                for idx, spot in results:
                    if spot['type'] != None:
                        folium.Marker([spot['lat'], spot['lon']], popup = spot['name'] + '\n\n(' + spot['type'] + ")", icon = folium.Icon(color = 'orange')).add_to(map_full)
                    else:
                        folium.Marker([spot['lat'], spot['lon']], popup = spot['name'], icon = folium.Icon(color = 'purple')).add_to(map_full)

            # Priority Recommendations. Hints.
            elif(len(hints) > 0):
                for hint in hints:
                    results = tourism[tourism['type'] == hint]
                    results['distance'] = haversineFunction([results['lat'], results['lon']], each)
                    results = results[results['distance'] < threshold]
                    results = results.iterrows()
                    for idx, spot in results:
                        if spot['type'] != None:
                           folium.Marker([spot['lat'], spot['lon']], popup = spot['name'] + '\n\n(' + spot['type'] + ")", icon = folium.Icon(color = 'orange')).add_to(map_full)
                        else:
                           folium.Marker([spot['lat'], spot['lon']], popup = spot['name'], icon = folium.Icon(color = 'purple')).add_to(map_full)


                        
        elif data == 'historic':
            # Recommend everything relevant from the category if no hints given.
            if(len(hints) == 0):
                results = historic
                results['distance'] = haversineFunction([results['lat'], results['lon']], each)
                results = results[results['distance'] < threshold]
                results = results.iterrows()
                for idx, spot in results:
                    if spot['type'] != None:
                        folium.Marker([spot['lat'], spot['lon']], popup = spot['name'] + '\n\n(' + spot['type'] + ")", icon = folium.Icon(color = 'purple')).add_to(map_full)
                    else:
                        folium.Marker([spot['lat'], spot['lon']], popup = spot['name'], icon = folium.Icon(color = 'purple')).add_to(map_full)

            # Priority Recommendations. Hints.
            elif(len(hints) > 0):
                for hint in hints:
                    results = historic
                    results = results[results['type'] == hint]
                    results['distance'] = haversineFunction([results['lat'], results['lon']], each)
                    results = results[results['distance'] < threshold]
                    results = results.iterrows()
                    if spot['type'] != None:
                        folium.Marker([spot['lat'], spot['lon']], popup = spot['name'] + '\n\n(' + spot['type'] + ")", icon = folium.Icon(color = 'purple')).add_to(map_full)
                    else:
                        folium.Marker([spot['lat'], spot['lon']], popup = spot['name'], icon = folium.Icon(color = 'purple')).add_to(map_full)

            
            
        elif data == 'food':
            # Recommend everything relevant from the category if no hints are given.
            if(len(hints) == 0):
                results = food
                results['distance'] = haversineFunction([results['lat'], results['lon']], each)
                results = results[results['distance'] < threshold]
                results = results.iterrows()
                for idx, spot in results:
                    if spot['cuisine'] != None:
                        folium.Marker([spot['lat'], spot['lon']], popup = spot['name'] + "\n\n(" + spot['amenity'] + " - " + spot['cuisine'] + ")", icon = folium.Icon(color = 'red')).add_to(map_full)
                    else:
                        folium.Marker([spot['lat'], spot['lon']], popup = spot['name'] + "\n\n(" + spot['amenity'] + ")", icon = folium.Icon(color = 'red')).add_to(map_full)


            # Priority Recommendations. Hints.
            elif(len(hints) > 0):
                for hint in hints:
                    results = food
                    results = results[results['amenity'] == hint]
                    results['distance'] = haversineFunction([results['lat'], results['lon']], each)
                    results = results[results['distance'] < threshold]
                    results = results.iterrows()
                    for idx, spot in results:
                        if spot['cuisine'] != None:
                            folium.Marker([spot['lat'], spot['lon']], popup = spot['name'] + "\n\n(" + spot['amenity'] + " - " + spot['cuisine'] + ")", icon = folium.Icon(color = 'red')).add_to(map_full)
                        else:
                            folium.Marker([spot['lat'], spot['lon']], popup = spot['name'] + "\n\n(" + spot['amenity'] + ")", icon = folium.Icon(color = 'red')).add_to(map_full)
                            
                         

        elif data == 'night':
            # Recommend everything relevant from the category if no hints given.
            if(len(hints) == 0):
                results = night
                results['distance'] = haversineFunction([results['lat'], results['lon']], each)
                results = results[results['distance'] < threshold]
                results = results.iterrows()
                for idx, spot in results:
                    if spot['amenity'] != None:
                        folium.Marker([spot['lat'], spot['lon']], popup = spot['name'] + "\n\n(" + spot['amenity'] + ")", icon = folium.Icon(color = 'cadetblue')).add_to(map_full)
                    else:
                        folium.Marker([spot['lat'], spot['lon']], popup = spot['name'], icon = folium.Icon(color = 'cadetblue')).add_to(map_full)
                        
            # Priority Recommendations. Hints.
            elif(len(hints) > 0):
                for hint in hints:
                    results = night
                    results = results[results['amenity'] == hint]
                    results['distance'] = haversineFunction([results['lat'], results['lon']], each)
                    results = results[results['distance'] < threshold]
                    results = results.iterrows()
                    for idx, spot in results:
                        if spot['amenity'] != None:
                            folium.Marker([spot['lat'], spot['lon']], popup = spot['name'] + "\n(" + spot['amenity'] + ')', icon = folium.Icon(color = 'cadetblue')).add_to(map_full)
                        else:
                            folium.Marker([spot['lat'], spot['lon']], popup = spot['name'], icon = folium.Icon(color = 'cadetblue')).add_to(map_full)
                            
                        

        elif data == 'entertainment':
            # Recommend everything relevant from the category if no hints given.
            if(len(hints) == 0):
                results = entertainment
                results['distance'] = haversineFunction([results['lat'], results['lon']], each)
                results = results[results['distance'] < threshold]
                results = results.iterrows()
                for idx, spot in results:    
                    if spot['amenity'] != None:
                        folium.Marker([spot['lat'], spot['lon']], popup = spot['name'] + "\n(" + spot['amenity'] + ')', icon = folium.Icon(color = 'pink')).add_to(map_full)
                    else:
                        folium.Marker([spot['lat'], spot['lon']], popup = spot['name'], icon = folium.Icon(color = 'pink')).add_to(map_full)
                            
            # Priority Recommendations. Hints.
            elif(len(hints) > 0):
                for hint in hints:
                    results = entertainment
                    results = results[results['amenity'] == hint]
                    results['distance'] = haversineFunction([results['lat'], results['lon']], each)
                    results = results[results['distance'] < threshold]
                    results = results.iterrows()
                    for idx, spot in results:
                        if spot['amenity'] != None:
                            folium.Marker([spot['lat'], spot['lon']], popup = spot['name'] + "\n(" + spot['amenity'] + ')', icon = folium.Icon(color = 'pink')).add_to(map_full)
                        else:
                            folium.Marker([spot['lat'], spot['lon']], popup = spot['name'], icon = folium.Icon(color = 'pink')).add_to(map_full)
                            

    mappath = "./map.html"
    map_full.save(mappath)
    webbrowser.open(mappath)

