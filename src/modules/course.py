class Course:
    def __init__(self, course_id, name, capacity):
        """
        Initialize a course with ID, name, and capacity.
        """
        self.course_id = course_id
        self.name = name
        self.capacity = capacity
        self.enrolled_students = []  # List of enrolled students
        self.instructor = None  # Assigned instructor

    def __str__(self):
        """
        String representation of a course.
        """
        instructor_name = self.instructor.name if self.instructor else "None"
        return f"Course ID: {self.course_id}, Name: {self.name}, Capacity: {self.capacity}, Instructor: {instructor_name}"