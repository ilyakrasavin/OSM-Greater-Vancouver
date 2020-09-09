#Distance function and any toher util funcitons I might need:
import numpy as np
import pandas as pd
import exifread as ef


#Distance function I used from ex3
def haversineFunction(cord1, cord2):
    #cord1[0] = lon1 cord1[1] = lat1
    #cord2[0] = lon2 cord2[1] = lat2


    p1 = np.sin((cord2[1]-cord1[1])/2)**2
    p2 = np.cos(cord1[1])
    p3 = np.cos(cord2[1])
    p4 = np.sin((cord2[0]-cord1[0])/2)**2
    p5 = p2 * p3 * p4
    h = p1 + p5
    #h = np.sin((lat2-lat1)/2)**2  +  np.cos(lat1)  *  np.cos(lat2)  * (np.sin((lon2-lon1)/2)**2)


    r = 6371
    return(2*r*np.arcsin(np.sqrt(h)))

    


#Get list of N closest points to cord1
#Input: cord1 [lon, lat](in radians), inputframe = dataframe with lon, lat, combineof the two
#Output: list of n elements of distance of n
def getDistanceListN(cord1, inputFrame, n):
    #Get distance with atleast one element in it
    distRange = 0.1
    i = 0
    #Bandage: convert back to degres this temporarily
    cordLat = (cord1[1]*180) / np.pi
    cordLon = (cord1[0]*180) / np.pi
    while(i < 6):
        #Filter for within range
        distFrame = inputFrame[ inputFrame["lat"] < (cordLat+distRange)]
        distFrame = distFrame[ distFrame["lat"] > (cordLat-distRange)]
        distFrame = distFrame[ distFrame["lon"] < (cordLon+distRange)]
        distFrame = distFrame[ distFrame["lon"] > (cordLon-distRange)]


        #Check that we have alteast n, max number of points, else increment
        if(distFrame["lon"].count() >= n):
            i = 6
        elif(distFrame["lon"].count() == inputFrame["lon"].count()):
            i = 6
        elif(i == 5):
            distFrame = inputFrame
            i = 6
        else:
            distRange = distRange * 10
            i = i+1

    
    #Now filter and get distances
    distFrame["distance"] = distFrame["combine"].apply( (lambda x: haversineFunction(x, cord1)))
    distFrame["distance"] =  distFrame["distance"] * 1000
    distFrame = distFrame.sort_values(by=["distance"])

    if(distFrame["distance"].count() <= n):
        return( distFrame["distance"].tolist())
    else:
        return( distFrame["distance"].tolist()[:n])

    
#Exif Gps extract code taken from:
#https://stackoverflow.com/a/45857824
#convert_to_degress function was borrowed from
#https://gist.github.com/snakeye/fdc372dbf11370fe29eb
def _convert_to_degress(value):
    """
    Helper function to conver the GPS coordinates stored in the EXIF to degress in float format
    :param value:
    :type value: exifread.utils.Ratio
    :rtype: float
    """
    d = float(value.values[0].num) / float(value.values[0].den)
    m = float(value.values[1].num) / float(value.values[1].den)
    s = float(value.values[2].num) / float(value.values[2].den)

    return d + (m / 60.0) + (s / 3600.0)

def getGPS(filepath):
    '''
    return gps data if present otherwise return empty dictionary
    '''
    with open(filepath, 'rb') as f:
        tags = ef.process_file(f)
        latitude = tags.get('GPS GPSLatitude')
        latitude_ref = tags.get('GPS GPSLatitudeRef')
        longitude = tags.get('GPS GPSLongitude')
        longitude_ref = tags.get('GPS GPSLongitudeRef')
                
        if latitude:
            lat_value = _convert_to_degress(latitude)
            if latitude_ref.values != 'N':
                lat_value = -lat_value
        else:
            return {}
        if longitude:
            lon_value = _convert_to_degress(longitude)
            if longitude_ref.values != 'E':
                lon_value = -lon_value
        else:
            return {}
        return{'latitude': lat_value, 'longitude':lon_value}
    return {}

