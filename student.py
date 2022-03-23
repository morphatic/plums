"""
Describes a Student in the PLuMS environment
"""

# import the parent class for Student
from person import Person


class Student(Person):
    def __init__(self, first_name, last_name, email_address, major="undecided"):
        # call the parent class constructor (Person) to setup basic properties
        Person.__init__(self, first_name, last_name, email_address)
        # add any Student-specific properties
        self.major = major
