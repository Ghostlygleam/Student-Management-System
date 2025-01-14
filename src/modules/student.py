class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.enrolled_courses = []  

    def add_course(self, course_name):
        #Add a course to the student's enrolled courses list
        self.enrolled_courses.append(course_name)
        
    def enroll_in_course(self, course):
        #Enroll the student in a course
        self.enrolled_courses.append(course.name)