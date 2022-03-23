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

    def that_has_a_display_name_that_updates_with_fn_and_ln():
        francis = Instructor("Francis", "Francison", "fran@example.com", "EnGeo 456")
        assert francis.name == "Francis Francison"
        francis.first_name = "Frankie"
        assert francis.name == "Frankie Francison"
