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
    
    def calculate_gpa(self):
        #Calculate the GPA based on the student's grades
        if not self.grades:
            return 0.0  

        grade_points = {
            'A': 4.0,
            'B': 3.0,
            'C': 2.0,
            'D': 1.0,
            'F': 0.0
        }

        total_points = 0
        total_courses = len(self.grades)

        for course_id, grade in self.grades.items():
            total_points += grade_points.get(grade, 0.0) 

        return total_points / total_courses
        
    def generate_transcript(self):
        #Generate an academic transcript for the student
        transcript = f"Academic Transcript for {self.name} (Student ID: {self.student_id}):\n"
        transcript += f"{'Course ID':<10}{'Grade':<10}\n"
        transcript += "-" * 20 + "\n"

        if not self.grades:
            transcript += "No grades available.\n"
        else:
            for course_id, grade in self.grades.items():
                transcript += f"{course_id:<10}{grade:<10}\n"

        gpa = self.calculate_gpa()
        transcript += f"\nGPA: {gpa:.2f}\n"

        return transcript
        

        
    