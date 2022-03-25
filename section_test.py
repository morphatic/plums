"""
Implements unit tests for the Section class
"""

from section import Section
from building import Building
from room import Room
from instructor import Instructor
from student import Student
from course import Course


def describe_a_course_section():

    # create buildings for things to happen
    king = Building("King")
    engeo = Building("EnGeo")
    # create offices and classrooms
    engeo2208 = Room(engeo, "2208", 12, 12)
    king341 = Room(king, "341", 10, 40)
    king337 = Room(king, "337", 25, 40)
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

    def that_has_a_course():
        assert isat252s2201.course.name == "ISAT252"
        assert morgan in isat252s2201.instructors
        assert len(isat252s2201.students) == 3

    def that_displays_basic_info():
        assert (
            isat252s2201.info
            == "ISAT252 S22 Programming and Problem Solving, Benton, MWF 9:10 (50 min)"
        )
