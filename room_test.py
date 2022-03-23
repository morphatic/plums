"""
Unit tests for the Room class
"""

from math import floor
from building import Building
from room import SQFT_PER_PERSON, Room


def describe_a_room():
    def that_has_a_building_number_length_width_and_capacity():
        """
        A room has a number (or maybe a name), a length and width
        in feet, and a capacity which is the number of
        people that can safely be in that room (according fire codes)
        """
        engeo = Building("EnGeo")
        my_office = Room(engeo, "123", 10, 10)
        assert my_office.number == "123"
        assert my_office.length == 10
        assert my_office.width == 10
        assert my_office.size == 100
        expected_capacity = floor(my_office.size / SQFT_PER_PERSON)
        assert my_office.capacity == expected_capacity
        assert my_office.name == "EnGeo 123"

        king = Building("King")
        a_classroom = Room(king, "337", 25, 40.5)
        assert a_classroom.size == 1012.5  # 1012.5 / 20 = 50.625
        expected_capacity = floor(a_classroom.size / SQFT_PER_PERSON)
        assert a_classroom.capacity == expected_capacity
        assert a_classroom.name == "King 337"
