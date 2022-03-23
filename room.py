"""
Implements the Room class for the PLuMS system
"""

from math import floor


SQFT_PER_PERSON = 20  # legal capacity of a room base on fire codes


class Room:
    """
    A room is a location where things take place. It could
    be, e.g., an office or classroom or lab, etc.
    """

    def __init__(self, building, number, length, width):
        self.building = building
        self.number = number
        self.length = length
        self.width = width

    @property
    def size(self):
        return self.length * self.width

    @property
    def capacity(self):
        return floor(self.size / SQFT_PER_PERSON)

    @property
    def name(self):
        return f"{self.building.name} {self.number}"
