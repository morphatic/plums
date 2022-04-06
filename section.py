"""
Implements a course section
"""


class Section:
    def __init__(
        self,
        course,
        semester,
        year,
        number,
        instructors,
        students,
        room,
        days,
        start_time,
        duration,
    ):
        self.course = course
        self.semester = semester
        self.year = year
        self.number = number
        self.instructors = instructors
        self.roster = students
        self.room = room
        self.days = days
        self.start_time = start_time
        self.duration = duration

    @property
    def info(self):
        return f"{self.course.name} {self.semester}{str(self.year)[-2:]} {self.number} {self.course.title}, {self.instructors[0].last_name}, {self.days} {self.start_time} ({self.duration} min)"
