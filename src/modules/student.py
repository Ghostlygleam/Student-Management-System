class Student:
    def __init__(self, student_id, name, email):
        """
        Initialize a student object with ID, name, and email.
        """
        self.student_id = student_id
        self.name = name
        self.email = email
        self.enrolled_courses = []  # List of courses the student is enrolled in

    def add_course(self, course_name):
        """
        Add a course to the student's enrolled courses list.
        """
        self.enrolled_courses.append(course_name)
        
    def enroll_in_course(self, course):
        """
        Enroll the student in a course.
        :param course: Instance of the Course class
        """
        self.enrolled_courses.append(course.name)