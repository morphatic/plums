"""
Unit tests for a Course object
"""

from course import Course


def describe_a_course():
    def that_has_a_subject_number_and_title():
        isat252 = Course("ISAT", "252", "Programming and Problem Solving")
        assert isat252.subject == "ISAT"
        assert isat252.number == "252"
        assert isat252.title == "Programming and Problem Solving"
        assert isat252.name == "ISAT 252"
        assert isat252.display_name == "ISAT 252: Programming and Problem Solving"
