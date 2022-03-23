"""
Defines the Person class that will be the base class
for Students and Instructors
"""


class Person:
    """
    The Person class is the base class for defining all
    people in the PLuMS environment, including Students
    and Instructors, and captures all of the basic properties
    common to both of these subclasses.
    """

    def __init__(self, first_name, last_name, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email_address

    @property
    def name(self):
        """
        Outputs the formatted name of the Person
        """
        return f"{self.first_name} {self.last_name}"
