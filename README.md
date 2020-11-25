# Recommendation System: OpenStreetMaps
Computational Data Science (CMPT 353) @ Simon Fraser University<br>

## About

The goal of this project was to become familiar with:<br>
1) Geospatial Data (OpenStreetMaps - Greater Vancouver Area)
2) Important Data Science procedures such as ETL, Descriptive Analysis and Visualization.<br>

Simple recommendation module developed in Python displays spots of interest based on geotagged pictures of a User's path.

## Contents

### /Datasets<br>
- Contains Datasets as Provided for the course in JSON format<br>
- WikiData Folder Contains additional data queried from Wikimedia Database<br>

### /Data Extraction<br>
- Scripts used to retrieve initial OpenStreetMaps Data for Greater Vancouver Area<br>

### /Project Pipeline<br>
- Jupyter Notebooks outlining the Progress
- Driver Program (main.py) and Supporting Python Scripts

## Requirements

The runnnable Python program relies on the following packages:

    pandas, numpy, PIL, folium, pathlib, exifread, webbrowser

## Launching
To Run the program, you will need to:
1. Put geotagged images of a walk into directory --> { ./ Project Pipeline / UserWalk / }

2. Locally Navigate to { ./Project Pipeline/ } 

3. Run the following command:

    To get recommendations based on your interests and travel mode [ walk | driving | transit ]. 
    
        python3 main.py [TourMode] [MoveMode] [Hints]
    The 'Hints' argument is optional. There is no limit on the number of hints you can pass it.<br> Omitting it will result in a general suggestion based on the broad interest (TourMode) defined by user:

    
    | TourMоde | Hints |
    | ------ | ------ |
    | entertainment | theatre, cinema, arts_centre, townhall, gambling, leisure, internet_cafe, lunch, bistro |
    | night | nightclub, pub, bar, events_venue |
    | tourism | hostel, motel, hotel, artwork, guest_house, attraction, museum, viewpoint, information, picnic_site, camp_site, caravan_site, gallery, theme_park, winery, lookout |
    | historic | monument, memorial, ruins, aircraft, boundary_stone, ship, milepost, milestone, building, tree, church, locomotive |
    | food | restaurant, cafe, fast_food, ice_cream, bistro, food_court |


    
    ### Example:
    This code will provide 'Nightlife' suggestions related to a path (images) stored in ./UserWalk directory.<br>
    User prefers to see _pubs_ and _bars_ in a _walking_ distance, thus passes it as hints.
    
        python3 main.py night walk pub bar
        
<p align="center">
  <img width="50%" height="50%" src="https://raw.githubusercontent.com/ilyakrasavin/OSM-Greater-Vancouver/master/sample_screen.png?token=AKGN4GQ2ZGKD6ZQDBEJHN227WEY3K">
</p>

## Credits
Ilia Krasavin (Data Transformation & Retrieval, Visualization Module)<br>
Stas Kalinowskii (Data Cleaning, Descriptive Analysis)<br>
Greg Baker (Course Instructor)
