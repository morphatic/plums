"""
Unit tests for reading data into the program
"""

import csv
from building import Building


def describe_data_import():
    def that_can_import_buildings():
        buildings = []  # empty list to hold our buildings
        building_file = open("data/buildings.csv", "r")
        building_reader = csv.reader(building_file)
        headers = next(
            building_reader
        )  # read the first line of the CSV file as column headers
        # loop through the rows
        for row in building_reader:
            # add a building to our list of buildings for each row
            buildings.append(Building(row[0]))
        assert len(buildings) == 4
