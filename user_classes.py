class Student:
    def __init__(self, name, student_id, email):
        self.name = name
        self.student_id = student_id
        self.email = email
        

class Instructor:
    def __init__(self, name, email, assigned_course):
        self.name = name
        self.email = email
        self.assigned_course = assigned_course

class Admin:
    def __init__(self, name, email):
        self.name = name
        self.email = email
