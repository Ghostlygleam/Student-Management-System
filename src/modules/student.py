class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.enrolled_courses = []
        self.grades = {}

    def enroll_in_course(self, course):
        self.enrolled_courses.append(course)

    def assign_grade(self, course_id, grade):
        self.grades[course_id] = grade

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

        total_points = sum(grade_points.get(grade, 0) for grade in self.grades.values())
        return total_points / len(self.grades)

    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Email: {self.email}"
