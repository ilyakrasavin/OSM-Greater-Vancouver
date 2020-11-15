import pandas as pd
import numpy as np
import PIL
import folium
import sys


# Input Checking
from pathlib import Path

# Image Exif data extraction and Utilities.
from utilHyp import haversineFunction, _convert_to_degress, getGPS

# Map Driver Program
from mapDriver import plotmap


# Launches the map on specified arguments.
def setup(tour_mode, hints, move_mode, imageWalk):

    if tour_mode.lower() == 'tourism':
        plotmap('tourism', hints, move_mode, imageWalk)
    elif tour_mode.lower() == 'historic':
        plotmap('historic', hints, move_mode, imageWalk)
    elif tour_mode.lower() == 'food':
        plotmap('food', hints, move_mode, imageWalk)
    elif tour_mode.lower() == 'night':
        plotmap('night', hints, move_mode, imageWalk)
    elif tour_mode.lower() == 'entertainment':
        plotmap('entertainment', hints, move_mode, imageWalk)



def main(tour_mode, move_mode, hints):

    user_locations = []
    
    # Open a directory
    ImagePath = Path('./UserWalk/').glob('*')

    # Search for Geoposition Data (EXif)
    for each in ImagePath:
        print(each)
        data = getGPS(each)
        if data == {}:
            print("\nNO GEODATA AVAILABLE FOR: " + str(each))
            continue

        data = (data.get('latitude'), data.get('longitude'))
        print(data)
        user_locations.append(data)

    if(len(user_locations) == 0):
        print("No data retreived from a path")

    # Launch
    setup(tour_mode, hints, move_mode, user_locations)

    return




if __name__ == "__main__":

    # Empty run
    if(len(sys.argv) < 2):
        print(sys.argv[0])
        print("\nNO OPTIONS PASSED!\nUSAGE: python3 main.py [TourMode] [MoveMode] [Hints]\n")
        exit(0)


    # User selects their interest
    if(sys.argv[1] in ['food', 'entertainment', 'tourism', 'historic', 'night']):
        tourMode = sys.argv[1]
    else:
        print("\nNo valid option 'TourMode' passed.\nERROR: " + sys.argv[1] + "\n")
        exit(0)

    # User Selects Mode of Transportation
    if(sys.argv[2] in ['walk', 'driving', 'transit']):
        moveMode = sys.argv[2]
    else:
        print("\nWrong Mode of Transportations set.")
        exit(0)

    user_hints = []
    # User provides hints
    if(len(sys.argv) > 3):
        for i in range(3, len(sys.argv)):
            user_hints.append(sys.argv[i])


    # Calling Main driver with no inference parameter.
    main(tourMode, moveMode, user_hints)
    