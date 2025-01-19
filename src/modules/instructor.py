class Instructor:
    def __init__(self, instructor_id, name, email):
        self.instructor_id = instructor_id
        self.name = name
        self.email = email

    def assign_grade(self, student, course_id, grade):
        if student:
            student.assign_grade(course_id, grade)
            print(f"Grade '{grade}' assigned to student '{student.name}' for course ID '{course_id}'.")

    def __str__(self):
        return f"Instructor ID: {self.instructor_id}, Name: {self.name}, Email: {self.email}"
