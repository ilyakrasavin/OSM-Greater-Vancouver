# OpenStreetMaps Recommendation System

## About

This term project was carried out in the scope of Computational Data Science Class @ Simon Fraser University.<br>
The goal was to familiarize ourselves with important procedures such as Data Retrieval, Transformation & Cleaning and Visualization.<br>
Geospatial Data from OpenStreetMaps for the area of Greater Vancouver is considered. Additional SQL requests were made to WikiMedia database in attempts to augment the dataset with images. While Augmentation failed due to lack of images for desired entries, the team has gained important experience transforming and cleaning existing data.<br>
As a result, we have designed a simple recommendation system using Folium in Python. It takes geotagged images and suggests spots of interest to a user on a Map.

## Contents

### /Datasets<br>
- Contains Datasets as Provided for the course in JSON format<br>
- WikiData Folder Contains additional data queried from Wikimedia Database

### /Data Extraction<br>
- Scripts used to retrieve initial OpenStreetMaps Data for Vancouver Area

### /Project Pipeline<br>
- Jupyter Notebooks Describing the Progress
- Driver Python Program and Support Scripts

## Requirements

The runnnable program relies on the following packages:

    pandas, numpy, PIL, folium, pathlib, exifread, webbrowser

## Launching
To Run the program, you will need to:
1. Put geotagged images of a walk into directory --> { ./ Project Pipeline / UserWalk / }

2. Locally Navigate to { ./Project Pipeline/ } 

3. Run the following command:

    To get recommendations based on your interests and travel mode [ walk | driving | transit ]. 
    
        python3 main.py [TourMode] [MoveMode] [Hints]
    The 'Hints' argument is optional. There is no limit on the number of hints you can pass it.<br> Omitting it will result in a general suggestion based on the broad interest defined by user:

    
    | TourMоde | Hints |
    | ------ | ------ |
    | entertainment | theatre, cinema, arts_centre, townhall, gambling, leisure, internet_cafe, lunch, bistro |
    | night | nightclub, pub, bar, events_venue |
    | tourism | hostel, motel, hotel, artwork, guest_house, attraction, museum, viewpoint, information, picnic_site, camp_site, caravan_site, gallery, theme_park, winery, lookout |
    | historic | monument, memorial, ruins, aircraft, boundary_stone, ship, milepost, milestone, building, tree, church, locomotive |
    | food | restaurant, cafe, fast_food, ice_cream, bistro, food_court |


    
    ### Example:
    This code will make 'Nightlife' suggestions related to path (images) stored in ./UserWalk directory.<br>
    User prefers to see pubs and bars, thus passes them as hints.
    
        python3 main.py night walk pub bar
        
<p align="center">
  <img width="50%" height="50%" src="https://raw.githubusercontent.com/ilyakrasavin/OSM-Greater-Vancouver/master/sample_screen.png?token=AKGN4GQ2ZGKD6ZQDBEJHN227WEY3K">
</p>

