class Student:
    def __init__(self, student_id: int, name: str, email: str):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.enrolled_courses = []
        self.grades = {}

    def enroll_in_course(self, course_id: int):
        if course_id not in self.enrolled_courses:
            self.enrolled_courses.append(course_id)

    def assign_grade(self, course_id: int, grade: str):
        self.grades[course_id] = grade

    def calculate_gpa(self) -> float:
        if not self.grades:
            return 0.0

        grade_points = {
            'A': 4.0,
            'B': 3.0,
            'C': 2.0,
            'D': 1.0,
            'F': 0.0
        }

        total_points = sum(grade_points.get(grade, 0.0) for grade in self.grades.values())
        total_courses = len(self.grades)

        return total_points / total_courses

    def generate_transcript(self) -> str:
        transcript_lines = [
            f"Academic Transcript for {self.name} (Student ID: {self.student_id}):",
            f"{'Course ID':<10}{'Grade':<10}",
            "-" * 20
        ]

        if not self.grades:
            transcript_lines.append("No grades available.")
        else:
            for course_id, grade in self.grades.items():
                transcript_lines.append(f"{course_id:<10}{grade:<10}")

        gpa = self.calculate_gpa()
        transcript_lines.append(f"\nGPA: {gpa:.2f}\n")

        return "\n".join(transcript_lines)

        

        
    