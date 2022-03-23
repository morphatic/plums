"""
Implements the Student class which is a
sub-class (or child class) of Person
"""

# import the Student class
from student import Student


def describe_a_student():
    def that_has_all_the_same_properties_as_a_person():
        bob = Student("Bob", "Robertson", "bob@example.com")
        assert bob.first_name == "Bob"
        assert bob.last_name == "Robertson"
        assert bob.email == "bob@example.com"

    def that_has_a_default_major_of_undecided():
        carl = Student("Carl", "Carlson", "carl@example.com")
        assert carl.major == "undecided"

    def that_can_have_a_specified_major():
        carl = Student("Carl", "Carlson", "carl@example.com", "ISAT")
        assert carl.major == "ISAT"

    def that_has_a_display_name_that_updates_with_fn_and_ln():
        gerry = Student("Gerry", "Gerryson", "gerry@example.com", "Math")
        assert gerry.name == "Gerry Gerryson"
        gerry.first_name = "Geraldine"
        assert gerry.name == "Geraldine Gerryson"
