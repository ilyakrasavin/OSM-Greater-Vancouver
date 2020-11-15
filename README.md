# OpenStreetMaps Recommendation System

## About

This Project leverages data manipulation and exploration tools on OpenStreetMaps data for the region of Greater Vancouver.


## Requirements

The runnnable program relies on the following packages:

    pandas, numpy, PIL, folium, pathlib, exifread, webbrowser

## Launching
To test the program, you will need to:
1. Put geotagged images of a walk into directory --> { ./ Project Pipeline / UserWalk / }

2. Locally Navigate to { ./Project Pipeline/ } 

2. Run the following commands:

    #### User controlled mode
    To get recommendations based on your interests and travel mode [ walk | driving | transit ]. 
    
        python3 main.py [TourMode] [MoveMode] [Hints]
    The 'Hints' option is optional. There is no limit on it either. Omitting it will result in a general suggestion based on the broad interest defined by user:

    
    | TourMоde | Hints |
    | ------ | ------ |
    | entertainment | theatre, cinema, arts_centre, townhall, gambling, leisure, internet_cafe, lunch, bistro |
    | night | nightclub, pub, bar, events_venue |
    | tourism | hostel, motel, hotel, artwork, guest_house, attraction, museum, viewpoint, information, picnic_site, camp_site, caravan_site, gallery, theme_park, winery, lookout |
    | historic | monument, memorial, ruins, aircraft, boundary_stone, ship, milepost, milestone, building, tree, church, locomotive |
    | food | restaurant, cafe, fast_food, ice_cream, bistro, food_court |


    
    #### Examples:
    This code will make 'night activity' suggestions related to path (images) stored in ./UserWalk directory.
    User prefers to see pubs and bars thus passes them as hints.
    
        python3 main.py night walk pub bar
        

<img src="https://raw.githubusercontent.com/ilyakrasavin/OSM-Greater-Vancouver/master/sample_screen.png?token=AKGN4GQ2ZGKD6ZQDBEJHN227WEY3K" width=50% height=50%>
