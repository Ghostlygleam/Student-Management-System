class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.enrolled_courses = []  
        self.grades = {}

    def add_course(self, course_name):
        #Add a course to the student's enrolled courses list
        self.enrolled_courses.append(course_name)
        
    def enroll_in_course(self, course):
        #Enroll the student in a course
        self.enrolled_courses.append(course.course_id)
    
    def assign_grade(self, course_id, grade):
        #Assign grade for students
        self.grades[course_id] = grade
        print(f"Grade '{grade}' has been assigned to student '{self.name}' for course ID '{course_id}'.")
        
        

        
    