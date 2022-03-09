"""
Implements the Instructor class
"""

from person import Person


class Instructor(Person):
    def __init__(self, first_name, last_name, email_address, office):
        Person.__init__(self, first_name, last_name, email_address)
        self.office = office
