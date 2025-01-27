class Instructor:
    def __init__(self, instructor_id, email):
        self.instructor_id = instructor_id
        self.email = email

    def assign_grade(self, student, course_id, grade):
        if student:
            student.assign_grade(course_id, grade)
            print(f"Grade '{grade}' assigned to student '{student.email}' for course ID '{course_id}'.")

    def __str__(self):
        return f"Instructor ID: {self.instructor_id}, Email: {self.email}"
