class Instructor:
    def __init__(self, instructor_id, name):
        """
        Initialize an instructor with ID and name.
        """
        self.instructor_id = instructor_id
        self.name = name

    def __str__(self):
        """
        String representation of the instructor.
        """
        return f"Instructor ID: {self.instructor_id}, Name: {self.name}"