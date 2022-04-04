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

    @pytest.fixture
    def students():
        """Load students from CSV"""
        student_data = read_csv("data/students.csv")
        students = []
        for i, s in student_data.iterrows():
            students.append(Student(s.FirstName, s.LastName, s.Email, s.Major))
        return students

    @pytest.fixture
    def instructors(rooms):
        """Load instructors from CSV"""
        instructor_data = read_csv("data/instructors.csv")
        instructors = []
        for i, t in instructor_data.iterrows():
            office = [r for r in rooms if r.name == t.Office]
            instructors.append(Instructor(t.FirstName, t.LastName, t.Email, office))
        return instructors

    def that_has_a_course(rooms, instructors, students):
        # get offices and classrooms from fixtures
        king337 = [r for r in rooms if r.name == "King 337"]
        # get instructor from fixtures
        morgan = [i for i in instructors if i.first_name == "Morgan"]
        # create a course
        isat252 = Course("ISAT", "252", "Programming and Problem Solving")

        # NOW create a sample section
        isat252s2201 = Section(
            isat252,
            "S",
            2022,
            [morgan],
            students,
            king337,
            "MWF",
            "9:10",
            "50",
        )
        assert isat252s2201.course.name == "ISAT252"
        assert morgan in isat252s2201.instructors
        assert len(isat252s2201.students) == len(students)

    # def that_displays_basic_info():
    #     assert (
    #         isat252s2201.info
    #         == "ISAT252 S22 Programming and Problem Solving, Benton, MWF 9:10 (50 min)"
    #     )
