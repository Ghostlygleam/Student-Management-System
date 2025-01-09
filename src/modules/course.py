class Course:
    def __init__(self, course_id, name, capacity):
        """
        Initialize a course with ID, name, and capacity.
        """
        self.course_id = course_id
        self.name = name
        self.capacity = capacity
        self.enrolled_students = []  # List of enrolled students

    def __str__(self):
        """
        String representation of a course.
        """
        return f"Course ID: {self.course_id}, Name: {self.name}, Capacity: {self.capacity}"