class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.enrolled_courses = []
        self.grades = {}

    def enroll_in_course(self, course):
        self.enrolled_courses.append(course.course_id)
        print(f"Student '{self.name}' enrolled in course '{course.name}'.")



    def assign_grade(self, course_id, grade):
        if course_id not in self.enrolled_courses:
            print(f"Cannot assign grade: Student is not enrolled in course {course_id}.")
            return  
        if course_id not in self.grades:
            self.grades[course_id] = []
        self.grades[course_id].append(grade)
        print(f"Grade '{grade}' assigned to student '{self.name}' for course ID '{course_id}'.")

    def calculate_gpa(self):
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
        total_grades = 0
        
        for grades in self.grades.values():
            for grade in grades:  
                total_points += grade_points.get(grade, 0)
                total_grades += 1

        if total_grades == 0:
            return 0.0

        return total_points / total_grades



    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Email: {self.email}"
