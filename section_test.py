"""
Implements unit tests for the Section class
"""

import pytest
from pandas import read_csv
from section import Section
from building import Building
from room import Room
from instructor import Instructor
from student import Student
from course import Course


def describe_a_course_section():
    @pytest.fixture
    def buildings():
        """Load buildings from CSV"""
        building_data = read_csv("data/buildings.csv")
        buildings = []
        for i, building in building_data.iterrows():
            buildings.append(Building(building.Name))
        return buildings

    @pytest.fixture
    def rooms(buildings):
        """Load rooms from CSV"""
        room_data = read_csv("data/rooms.csv")
        rooms = []
        for i, room in room_data.iterrows():
            building = [b for b in buildings if b.name == room.Building][0]
            rooms.append(Room(building, room.Number, room.Length, room.Width))
        return rooms

    def that_has_a_course(rooms):
        # get offices and classrooms from fixtures
        engeo2208 = [r for r in rooms if r.name == "EnGeo 2208"]
        king341 = [r for r in rooms if r.name == "King 341"]
        king337 = [r for r in rooms if r.name == "King 337"]
        # create students and instructors to populate the section
        morgan = Instructor("Morgan", "Benton", "morgan@example.edu", engeo2208)
        teate = Instructor("Anthony", "Teate", "teate@example.edu", king341)
        alice = Student("Alice", "Alison", "alice@example.edu", "ISAT")
        bob = Student("Bob", "Bobson", "bob@example.edu")
        charlie = Student("Charlie", "Charlieson", "charlie@example.edu", "CIS")
        # create a course
        isat252 = Course("ISAT", "252", "Programming and Problem Solving")

        # NOW create a sample section
        isat252s2201 = Section(
            isat252,
            "S",
            2022,
            [morgan],
            [alice, bob, charlie],
            king337,
            "MWF",
            "9:10",
            "50",
        )
        assert isat252s2201.course.name == "ISAT252"
        assert morgan in isat252s2201.instructors
        assert len(isat252s2201.students) == 3

    # def that_displays_basic_info():
    #     assert (
    #         isat252s2201.info
    #         == "ISAT252 S22 Programming and Problem Solving, Benton, MWF 9:10 (50 min)"
    #     )
