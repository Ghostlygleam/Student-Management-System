class Instructor:
    def __init__(self, instructor_id, name):
        self.instructor_id = instructor_id
        self.name = name
        
    def assign_grade(self, course, student, grade):
        #Assign grade for specific course
        if student.student_id not in course.enrolled_students:
            print(f"Student '{student.name}' is not enrolled in course '{course.name}'.")
        else:
            student.assign_grade(course.course_id, grade)
            print(f"Grade '{grade}' has been assigned by instructor '{self.name}' to student '{student.name}' for course '{course.name}'.")

    def __str__(self):
        return f"Instructor ID: {self.instructor_id}, Name: {self.name}"
    
    