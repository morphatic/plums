"""
Unit tests for the Room class
"""

from room import Room


def describe_a_room():
    def that_has_a_number_length_width_and_capacity():
        """
        A room has a number (or maybe a name), a length and width
        in square feet, and a capacity which is the number of
        people that can safely be in that room (according fire codes)
        """
        my_office = Room("123", 10, 10)
        assert my_office.number == "123"
        assert my_office.length == 10
        assert my_office.width == 10
        assert my_office.capacity == 5
        assert my_office.size == 100

        a_classroom = Room("337", 25, 40.5)
        assert a_classroom.size == 1012.5
        assert a_classroom.capacity == 50
