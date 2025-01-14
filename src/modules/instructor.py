class Instructor:
    def __init__(self, instructor_id, name):
        self.instructor_id = instructor_id
        self.name = name

    def __str__(self):
        return f"Instructor ID: {self.instructor_id}, Name: {self.name}"