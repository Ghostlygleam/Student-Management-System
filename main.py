import csv
import os
from src.utils.auth_service import Authentication
from src.utils.course_service import (
    add_course,
    edit_course,
    delete_course,
    enroll_student_in_course,
    unenroll_student_in_course,
    view_enrolled_students,
    assign_instructor_to_course,
    assign_grade_to_student,
    display_student_gpa,
    display_transcript,
    generate_course_list
)
from src.modules.course import Course
from src.modules.student import Student
from src.modules.instructor import Instructor

# Global Variables
auth = Authentication()
course_list = []
instructor_list = []
student_list = []
user_file = os.path.join(os.getcwd(), "users.csv")


def load_users():
    """
    Load all user profiles from a CSV file and update authentication system.
    """
    print(f"Loading users from {user_file}...")
    try:
        with open(user_file, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                role = row["role"].lower()
                email = row["email"]
                name = row["name"]
                user_id = int(row["id"])

                # Добавляем пользователя в соответствующий список
                if role == "student":
                    student = Student(student_id=user_id, name=name, email=email)
                    student_list.append(student)
                elif role == "instructor":
                    instructor = Instructor(instructor_id=user_id, name=name, email=email)
                    instructor_list.append(instructor)

                # Добавляем пользователя в систему аутентификации
                auth.users[email] = {"password": "1", "role": role}  # Здесь можно использовать реальные пароли, если они есть в файле

        print("Users successfully loaded.")
    except FileNotFoundError:
        print(f"User file not found at {user_file}. Starting with an empty user list.")
    except Exception as e:
        print(f"Error loading users: {e}")



def save_users():
    print("Attempting to save users...")
    try:
        with open(user_file, "w", newline="") as file:
            fieldnames = ["id", "name", "email", "password", "role"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            # Сохранение студентов
            for student in student_list:
                writer.writerow({
                    "id": student.student_id,
                    "name": student.name,
                    "email": student.email,
                    "password": "hashed_password",  # Заменить на реальное значение
                    "role": "student"
                })

            # Сохранение инструкторов
            for instructor in instructor_list:
                writer.writerow({
                    "id": instructor.instructor_id,
                    "name": instructor.name,
                    "email": instructor.email,
                    "password": "hashed_password",  # Заменить на реальное значение
                    "role": "instructor"
                })

        print(f"Users successfully saved to {user_file}.")
    except Exception as e:
        print(f"Error saving users to {user_file}: {e}")






def admin_menu():
    """
    Admin menu for managing courses, instructors, and profiles.
    """
    while True:
        print("\nAdmin Menu:")
        print("===========================")
        print("1. Add Course")
        print("2. Edit Course")
        print("3. Delete Course")
        print("4. Manage User Profiles")
        print("5. Manage Instructors")
        print("6. View Course Statistics")
        print("7. Logout")
        print("===========================")
        action = input("Choose an option: ")

        if action == "1":
            course_id = int(input("Enter course ID: "))
            name = input("Enter course name: ")
            capacity = int(input("Enter course capacity: "))
            add_course(course_list, course_id, name, capacity)

        elif action == "2":
            course_id = int(input("Enter course ID to edit: "))
            new_name = input("Enter new course name (leave empty to skip): ") or None
            try:
                new_capacity = int(input("Enter new course capacity (leave empty to skip): ") or 0)
            except ValueError:
                new_capacity = None
            edit_course(course_list, course_id, new_name, new_capacity)

        elif action == "3":
            course_id = int(input("Enter course ID to delete: "))
            delete_course(course_list, course_id)

        elif action == "4":
            manage_profiles()

        elif action == "5":
            manage_instructors()

        elif action == "6":
            generate_course_list(course_list)

        elif action == "7":
            print("Logging out...")
            break

        else:
            print("Invalid option. Please choose again.")


def manage_profiles():
    """
    Menu for managing student profiles.
    """
    global student_list
    while True:
        print("\nManage Profiles:")
        print("===========================")
        print("1. Add Profile")
        print("2. Edit Profile")
        print("3. Delete Profile")
        print("4. View All Profiles")
        print("5. Back to Admin Menu")
        print("===========================")
        action = input("Choose an option: ")

        if action == "1":
            name = input("Enter the student's name: ")
            student_id = int(input("Enter the student's ID: "))
            email = input("Enter the student's email: ")
            password = input("Set a password for this student: ")

            if email and password:
                # Register user in the authentication system
                auth.register_user(email, password, "student")
                
                # Add student to the student list
                student_list.append(Student(name=name, student_id=student_id, email=email))
                print("Saving users to file...")
                save_users()
                print("Save completed.")
                print(f"Student profile for {name} added successfully and is ready for login.")
            else:
                print("Email and password are required to create a profile.")

        elif action == "2":
            email = input("Enter the email of the profile to edit: ")
            student = next((s for s in student_list if s.email == email), None)
            if student:
                new_name = input("Enter new name (leave empty to skip): ") or student.name
                student.name = new_name
                print("Saving users to file...")
                save_users()
                print("Save completed.")
                print(f"Profile for {email} updated successfully.")
            else:
                print("Profile not found.")

        elif action == "3":
            email = input("Enter the email of the profile to delete: ")
            student_list = [s for s in student_list if s.email != email]
            print("Saving users to file...")
            save_users()
            print("Save completed.")
            print(f"Profile with email {email} has been deleted.")

        elif action == "4":
            print("\nAll Profiles:")
            for student in student_list:
                print(f"ID: {student.student_id}, Name: {student.name}, Email: {student.email}")

        elif action == "5":
            print("Returning to Admin Menu...")
            break

        else:
            print("Invalid option. Please choose again.")




def manage_instructors():
    """
    Menu for managing instructors.
    """
    while True:
        print("\nManage Instructors:")
        print("===========================")
        print("1. Add Instructor")
        print("2. Assign Instructor to Course")
        print("3. View All Instructors")
        print("4. Back to Admin Menu")
        print("===========================")
        action = input("Choose an option: ")

        if action == "1":
            instructor_id = int(input("Enter instructor ID: "))
            name = input("Enter instructor name: ")
            email = input("Enter instructor email: ")
            password = input("Set a password for this instructor: ")

            if email and password:
                auth.register_user(email, password, "instructor")
                instructor_list.append(Instructor(instructor_id=instructor_id, name=name, email=email))
                print("Saving users to file...")
                save_users()
                print("Save completed.")
                print(f"Instructor '{name}' added successfully and is ready for login.")
            else:
                print("Email and password are required to create an instructor profile.")

        elif action == "2":
            instructor_id = int(input("Enter instructor ID: "))
            course_id = int(input("Enter course ID: "))
            instructor = next((i for i in instructor_list if i.instructor_id == instructor_id), None)
            course = next((c for c in course_list if c.course_id == course_id), None)

            if instructor and course:
                assign_instructor_to_course(course, instructor)
            else:
                print("Invalid instructor or course ID.")

        elif action == "3":
            print("\nList of Instructors:")
            for instructor in instructor_list:
                print(f"Instructor ID: {instructor.instructor_id}, Name: {instructor.name}, Email: {instructor.email}")

        elif action == "4":
            print("Returning to Admin Menu...")
            break

        else:
            print("Invalid option. Please choose again.")


def instructor_menu(email):
    """
    Instructor menu for managing courses and grades.
    """
    current_instructor = next((i for i in instructor_list if i.email == email), None)
    if not current_instructor:
        print("Instructor profile not found.")
        return

    while True:
        print("\nInstructor Menu:")
        print("===========================")
        print("1. Assign Grade to Student")
        print("2. View Enrolled Students in a Course")
        print("3. Logout")
        print("===========================")
        action = input("Choose an option: ")

        if action == "1":
            course_id = int(input("Enter course ID: "))
            student_id = int(input("Enter student ID: "))
            grade = input("Enter grade (A-F): ")
            course = next((c for c in course_list if c.course_id == course_id), None)
            student = next((s for s in student_list if s.student_id == student_id), None)

            if course and student:
                assign_grade_to_student(student, course_id, grade)
            else:
                print("Invalid course ID or student ID.")

        elif action == "2":
            course_id = int(input("Enter course ID: "))
            course = next((c for c in course_list if c.course_id == course_id), None)
            if course:
                view_enrolled_students(course, student_list)
            else:
                print("Invalid course ID.")

        elif action == "3":
            print("Logging out...")
            break

        else:
            print("Invalid option. Please choose again.")


def student_menu(email):
    """
    Student menu for viewing and managing personal information.
    """
    current_student = next((s for s in student_list if s.email == email), None)
    if not current_student:
        print("Student profile not found.")
        return

    while True:
        print("\nStudent Menu:")
        print("===========================")
        print("1. Enroll in a Course")
        print("2. View Grades and Transcript")
        print("3. Logout")
        print("===========================")
        action = input("Choose an option: ")

        if action == "1":
            course_id = int(input("Enter course ID to enroll in: "))
            course = next((c for c in course_list if c.course_id == course_id), None)
            if course:
                enroll_student_in_course(course, current_student)
            else:
                print("Invalid course ID.")

        elif action == "2":
            display_transcript(current_student)

        elif action == "3":
            print("Logging out...")
            break

        else:
            print("Invalid option. Please choose again.")


def authentication_menu():
    """
    Menu for user authentication and role-based access.
    """
    while True:
        print("\nAuthentication Menu:")
        print("===========================")
        print("1. Register User")
        print("2. Login")
        print("3. Exit")
        print("===========================")
        action = input("Choose an option: ")

        if action == "1":  # Регистрация нового пользователя
            username = input("Enter your username: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            role = input("Enter your role (admin/student/instructor): ").lower()

            if email and password:
                # Вызываем функцию register_user для регистрации
                register_user(email, password, role)
            else:
                print("Email and password are required for registration.")

        elif action == "2":  # Вход в систему
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            role = auth.login_user(email, password)

            if role == "admin":
                admin_menu()
            elif role == "student":
                student_menu(email)
            elif role == "instructor":
                instructor_menu(email)
            else:
                print("Invalid role or authentication failed.")

        elif action == "3":  # Выход из системы
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid option. Please choose again.")

            
def register_user(email, password, role):
    global student_list, instructor_list
    if email in auth.users:
        print(f"User '{email}' already exists!")
        return

    # Генерация ID
    if role == "student":
        student_id = len(student_list) + 1
        student = Student(student_id=student_id, name="Student Name", email=email)
        student_list.append(student)
    elif role == "instructor":
        instructor_id = len(instructor_list) + 1
        instructor = Instructor(instructor_id=instructor_id, name="Instructor Name", email=email)
        instructor_list.append(instructor)
    elif role == "admin":
        print(f"Registering admin with email {email}.")
        auth.users[email] = {"password": password, "role": "admin"}  # Добавляем администратора в память
    else:
        print("Invalid role specified. Please choose 'student', 'instructor', or 'admin'.")
        return

    # Добавляем пользователя в CSV через auth.register_user
    print(f"Attempting to register user: email={email}, password={password}, role={role}")
    auth.register_user(email, password, role)  # Сохраняем в CSV через Authentication
    save_users()  # Обновляем основной users.csv
    print(f"User '{email}' registered successfully!")





if __name__ == "__main__":
    authentication_menu()
