import csv
import os
import hashlib
from src.modules.student import Student
from src.modules.instructor import Instructor
from src.modules.admin import Admin
from src.utils.auth_service import Authentication
from src.modules.course import Course

# File paths
user_file = os.path.join(os.getcwd(), "users.csv")
course_file = os.path.join(os.getcwd(), "courses.csv")

# Global data
student_list = []
instructor_list = []
course_list = []

auth = Authentication(user_file)


def load_courses():
    print(f"Loading courses from {course_file}...")

    try:
        with open(course_file, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                course_id = int(row.get("id", 0))
                name = row.get("name", "").strip()
                capacity = int(row.get("capacity", 0))

                if not course_id or not name or not capacity:
                    print(f"Invalid course data found: {row}. Skipping...")
                    continue

                instructor_email = row.get("instructor_email", "").strip()
                course = Course(course_id=course_id, name=name, capacity=capacity)
                course.instructor = instructor_email if instructor_email else None
                course_list.append(course)

                print(f"Loaded course: {course.name} (ID: {course_id})")
        
        print("All courses loaded successfully.")

    except FileNotFoundError:
        print(f"Course file {course_file} not found. Starting with an empty course list.")
    except Exception as err:
        print(f"Error loading courses: {err}")

    print("Courses currently in memory:")
    for course in course_list:
        print(f"- {course.name} (ID: {course.course_id}, Capacity: {course.capacity})")

def save_courses(courses, file_path):
    if not courses:
        print("Nothing to save. No courses provided.")
        return

    print("Saving courses to file...")
    try:
        # Ensure directory exists
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(file_path, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "name", "capacity", "instructor_email"])
            writer.writeheader()

            for c in courses:  
                writer.writerow({
                    "id": c.course_id,
                    "name": c.name,
                    "capacity": c.capacity,
                    "instructor_email": c.instructor or ""
                })

        print("Courses saved.")

    except PermissionError:
        print("Cannot save courses. Permission denied.")
    except Exception as ex:  
        print(f"Failed to save courses: {ex}")

def load_users():
    print(f"Loading users from file: {user_file}")
    try:
        with open(user_file, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                role = row.get("role", "").strip().lower()
                email = row.get("email", "").strip()
                name = row.get("name", "Unnamed User").strip()
                user_id = row.get("id", 0)

                if not role or not email or not user_id:
                    print(f"Skipping invalid user entry: {row}")
                    continue

                try:
                    user_id = int(user_id)
                except ValueError:
                    print(f"Invalid user ID '{user_id}' for entry: {row}")
                    continue

                if role == "student":
                    student = Student(student_id=user_id, name=name, email=email)
                    student_list.append(student)
                elif role == "instructor":
                    instructor = Instructor(instructor_id=user_id, name=name, email=email)
                    instructor_list.append(instructor)
                else:
                    print(f"Unknown role '{role}' for user: {row}")
                    continue

                auth.users[email] = {"password": row.get("password", ""), "role": role}

        print("All users have been loaded.")

    except FileNotFoundError:
        print(f"User file '{user_file}' not found. Starting with an empty user list.")
    except Exception as ex:
        print(f"An unexpected error occurred while loading users: {ex}")


def save_users():
    print("Starting user save process...")
    try:
        with open(user_file, mode="w", newline="") as file:
            fieldnames = ["id", "name", "email", "password", "role"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            # Save students
            for student in student_list:
                writer.writerow({
                    "id": student.student_id,
                    "name": student.name,
                    "email": student.email,
                    "password": auth.users.get(student.email, {}).get("password", ""),
                    "role": "student"
                })

            # Save instructors
            for instructor in instructor_list:
                writer.writerow({
                    "id": instructor.instructor_id,
                    "name": instructor.name,
                    "email": instructor.email,
                    "password": auth.users.get(instructor.email, {}).get("password", ""),
                    "role": "instructor"
                })

            # Save administrators
            for email, data in auth.users.items():
                if data.get("role") == "admin":
                    writer.writerow({
                        "id": "0",  # Fixed ID for admin
                        "name": "Admin",
                        "email": email,
                        "password": data.get("password", ""),
                        "role": "admin"
                    })

        print(f"Users saved successfully to {user_file}.")
    except PermissionError:
        print(f"Permission denied: Unable to write to {user_file}.")
    except Exception as ex:
        print(f"Unexpected error during user save process: {ex}")

        
def register_user(email, password, role):
    global student_list, instructor_list

    if email in auth.users:
        print(f"Error: User with email '{email}' already exists.")
        return

    if role == "student":
        student_id = len(student_list) + 1
        student = Student(student_id=student_id, name="Unnamed Student", email=email)
        student_list.append(student)
        print(f"New student registered with email: {email}, ID: {student_id}.")
    elif role == "instructor":
        instructor_id = len(instructor_list) + 1
        instructor = Instructor(instructor_id=instructor_id, name="Unnamed Instructor", email=email)
        instructor_list.append(instructor)
        print(f"New instructor registered with email: {email}, ID: {instructor_id}.")
    elif role == "admin":
        print(f"Admin registration initiated for email: {email}.")
        auth.users[email] = {"password": hashlib.sha256(password.encode()).hexdigest(), "role": "admin"}
    else:
        print("Invalid role. Allowed roles: 'student', 'instructor', 'admin'.")
        return

    # Add user to authentication system
    auth.register_user(email, password, role)
    print(f"User '{email}' successfully registered as '{role}'.")
    
    # Save users to persist changes
    save_users()


def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("===========================")
        print("1. View All Users")
        print("2. Add New User")
        print("3. View All Courses")
        print("4. Add New Course")
        print("5. Assign Instructor to Course")
        print("6. Logout")
        print("===========================")
        action = input("Select an option (1-6): ")

        if action == "1":
            if not auth.users:
                print("No registered users found.")
            else:
                print("\nRegistered Users:")
                for email, data in auth.users.items():
                    print(f"Email: {email}, Role: {data['role']}")

        elif action == "2":
            email = input("Enter new user's email: ").strip()
            password = input("Enter new user's password: ").strip()
            role = input("Enter new user's role (admin/student/instructor): ").strip().lower()
            if role not in ["admin", "student", "instructor"]:
                print("Invalid role. Please choose from 'admin', 'student', or 'instructor'.")
            else:
                register_user(email, password, role)

        elif action == "3":
            if not course_list:
                print("No courses available.")
            else:
                print("\nAll Courses:")
                for course in course_list:
                    instructor = course.instructor or "None"
                    print(f"ID: {course.course_id}, Name: {course.name}, Capacity: {course.capacity}, Instructor: {instructor}")

        elif action == "4":
            name = input("Enter course name: ").strip()
            try:
                capacity = int(input("Enter course capacity: "))
                course_id = len(course_list) + 1
                course = Course(course_id=course_id, name=name, capacity=capacity)
                course_list.append(course)
                save_courses()
                print(f"Course '{name}' added successfully.")
            except ValueError:
                print("Invalid input for course capacity. Please enter a number.")

        elif action == "5":
            try:
                course_id = int(input("Enter course ID: "))
                instructor_email = input("Enter instructor's email: ").strip()
                course = next((c for c in course_list if c.course_id == course_id), None)
                instructor = next((i for i in instructor_list if i.email == instructor_email), None)

                if not course:
                    print(f"Course with ID {course_id} does not exist.")
                elif not instructor:
                    print(f"Instructor with email {instructor_email} does not exist.")
                else:
                    course.instructor = instructor_email
                    save_courses()
                    print(f"Instructor '{instructor_email}' assigned to course '{course.name}'.")
            except ValueError:
                print("Invalid input. Course ID must be a number.")

        elif action == "6":
            print("Logging out of the Admin Panel...")
            break

        else:
            print("Invalid selection. Please choose a valid option (1-6).")



def student_menu(student_email):
    # Find the current student by email
    current_student = next((s for s in student_list if s.email == student_email), None)
    if not current_student:
        print("Student profile not found. Please contact the administrator.")
        return

    while True:
        print("\nStudent Menu:")
        print("===========================")
        print("1. View Enrolled Courses")
        print("2. Enroll in a Course")
        print("3. View Grades and GPA")
        print("4. Logout")
        print("===========================")
        action = input("Select an option (1-4): ").strip()

        if action == "1":
            print("\nEnrolled Courses:")
            if current_student.enrolled_courses:
                for course in current_student.enrolled_courses:
                    print(f"- {course}")
            else:
                print("You are not enrolled in any courses yet.")

        elif action == "2":
            course_name = input("Enter the name of the course to enroll in: ").strip()
            course = next((c for c in course_list if c.name.lower() == course_name.lower()), None)

            if not course:
                print(f"Course '{course_name}' does not exist. Please check the course name.")
            elif len(course.enrolled_students) >= course.capacity:
                print(f"Course '{course.name}' is full. Enrollment is not possible.")
            elif course.name in current_student.enrolled_courses:
                print(f"You are already enrolled in '{course.name}'.")
            else:
                current_student.enroll_in_course(course.name)
                course.enrolled_students.append(current_student)
                print(f"You have successfully enrolled in '{course.name}'.")
                save_courses()

        elif action == "3":
            print("\nYour Grades:")
            if current_student.grades:
                for course_id, grade in current_student.grades.items():
                    print(f"Course: {course_id}, Grade: {grade}")
            else:
                print("No grades available yet.")
            gpa = current_student.calculate_gpa()
            print(f"Your GPA: {gpa:.2f}")

        elif action == "4":
            print("Logging out of the Student Dashboard...")
            break

        else:
            print("Invalid selection. Please choose a valid option.")

def instructor_menu(instructor_email):
    # Find the current instructor by email
    current_instructor = next((i for i in instructor_list if i.email == instructor_email), None)
    if not current_instructor:
        print("Instructor profile not found. Please contact the administrator.")
        return

    while True:
        print("\nInstructor Menu:")
        print("===========================")
        print("1. View Assigned Courses")
        print("2. Assign Grade to Student")
        print("3. Logout")
        print("===========================")
        action = input("Select an option (1-3): ").strip()

        if action == "1":
            print("\nAssigned Courses:")
            assigned_courses = [
                course for course in course_list 
                if course.instructor and course.instructor.lower() == instructor_email.lower()
            ]
            if assigned_courses:
                for course in assigned_courses:
                    print(f"Course ID: {course.course_id}, Name: {course.name}, Capacity: {course.capacity}")
            else:
                print("You have not been assigned to any courses yet.")

        elif action == "2":
            student_email = input("Enter the email of the student: ").strip()
            try:
                course_id = int(input("Enter the course ID: ").strip())
                grade = input("Enter the grade (A-F): ").strip().upper()

                student = next((s for s in student_list if s.email == student_email), None)
                course = next((c for c in course_list if c.course_id == course_id), None)

                if not student:
                    print(f"Student with email '{student_email}' not found.")
                elif not course:
                    print(f"Course with ID '{course_id}' not found.")
                elif course.instructor and course.instructor.lower() != instructor_email.lower():
                    print(f"You are not assigned to the course '{course.name}'.")
                elif grade not in ["A", "B", "C", "D", "F"]:
                    print("Invalid grade. Please enter a grade from A to F.")
                else:
                    current_instructor.assign_grade(student, course_id, grade)
                    print(f"Grade '{grade}' assigned to student '{student.name}' for course '{course.name}'.")
            except ValueError:
                print("Invalid input. Course ID must be a valid number.")

        elif action == "3":
            print("Logging out of Instructor Dashboard...")
            break

        else:
            print("Invalid selection. Please choose a valid option (1-3).")

def authentication_menu():
    while True:
        print("\nAuthentication Menu:")
        print("===========================")
        print("1. Register User")
        print("2. Login")
        print("3. Exit")
        print("===========================")
        action = input("Select an option (1-3): ").strip()

        if action == "1":
            email = input("Enter your email: ").strip()
            password = input("Enter your password: ").strip()
            role = input("Enter your role (admin/student/instructor): ").strip().lower()

            if not email or not password:
                print("Email and password cannot be empty.")
            elif role not in ["admin", "student", "instructor"]:
                print("Invalid role. Please choose 'admin', 'student', or 'instructor'.")
            else:
                register_user(email, password, role)

        elif action == "2":
            email = input("Enter your email: ").strip()
            password = input("Enter your password: ").strip()

            if not email or not password:
                print("Email and password are required for login.")
                continue

            role = auth.login_user(email, password)

            if role == "admin":
                print(f"Welcome, admin {email}!")
                admin_menu()
            elif role == "student":
                print(f"Welcome, student {email}!")
                student_menu(email)
            elif role == "instructor":
                print(f"Welcome, instructor {email}!")
                instructor_menu(email)
            else:
                print("Authentication failed. Please check your credentials.")

        elif action == "3":
            print("Goodbye! Exiting the system.")
            break

        else:
            print("Invalid selection. Please choose a valid option (1-3).")

if __name__ == "__main__":
    load_users()
    load_courses()
    authentication_menu()