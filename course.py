"""
Defines a Course in PLuMS
"""


class Course:
    def __init__(self, subject, number, title):
        self.subject = subject
        self.number = number
        self.title = title

    @property
    def name(self):
        return f"{self.subject} {self.number}"

    @property
    def display_name(self):
        return f"{self.name}: {self.title}"
