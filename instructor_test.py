"""
Unit tests for the Instructor class
"""

from instructor import Instructor


def describe_an_instructor():
    def that_has_all_the_same_properties_as_a_person():
        david = Instructor("David", "Davidson", "david@example.com", "A 1")
        assert david.first_name == "David"
        assert david.last_name == "Davidson"
        assert david.email == "david@example.com"

    def that_has_an_office():
        ernie = Instructor("Ernie", "Ernieson", "ernie@example.com", "King 123")
        assert ernie.office == "King 123"
