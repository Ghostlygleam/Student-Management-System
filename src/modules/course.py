class Course:
    def __init__(self, course_id, name, capacity):
        self.course_id = course_id
        self.name = name
        self.capacity = capacity
        self.enrolled_students = []
        self.instructor = None

    def __str__(self):
        return f"ID: {self.course_id}, Name: {self.name}, Capacity: {self.capacity}, Instructor: {self.instructor or 'None'}"

