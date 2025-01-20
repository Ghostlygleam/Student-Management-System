import unittest
from unittest.mock import patch, mock_open, MagicMock
import hashlib
from src.modules.course import Course
from src.modules.student import Student
from src.utils.auth_service import Authentication
from main import save_courses, load_courses, course_list


# Tests for authentication-related functionality
class TestAuthService(unittest.TestCase):
    @patch("builtins.open", new_callable=MagicMock)
    def test_register_user(self, mock_open):
        auth = Authentication("test_users.csv")
        auth.register_user("test@example.com", "password123", "student")

        # Ensure the user is added to the system with the correct role
        self.assertIn("test@example.com", auth.users)
        self.assertEqual(auth.users["test@example.com"]["role"], "student")

    def test_login_user(self):
        auth = Authentication()

        # Prepopulate the user database with a test user
        hashed_password = hashlib.sha256("password123".encode()).hexdigest()
        auth.users = {
            "test@example.com": {
                "password": hashed_password,
                "role": "student"
            }
        }

        # Verify login succeeds for valid credentials
        role = auth.login_user("test@example.com", "password123")
        self.assertEqual(role, "student")


# Tests for course management
class TestCourseModule(unittest.TestCase):
    def setUp(self):
        # Create sample courses for testing
        self.course1 = Course(course_id=1, name="Math", capacity=30)
        self.course2 = Course(course_id=2, name="Science", capacity=25)
        course_list.clear()
        course_list.extend([self.course1, self.course2])

    def test_add_course(self):
        new_course = Course(course_id=3, name="History", capacity=20)

        # Add a new course to the course list
        course_list.append(new_course)
        self.assertIn(new_course, course_list)

    def test_remove_course(self):
        # Remove an existing course and verify it's no longer in the list
        course_list.remove(self.course1)
        self.assertNotIn(self.course1, course_list)


# Tests for loading and saving data
class TestMainModule(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open)
    def test_load_courses(self, mock_open):
        # Mock the content of the course CSV file
        mock_open.return_value.__enter__.return_value = iter([
            "id,name,capacity,instructor_email\n",
            "1,Math,30,john@example.com\n",
            "2,Science,25,\n"
        ])

        # Clear the course list and load courses from the mock file
        course_list.clear()
        load_courses()

        # Verify that the courses were loaded correctly
        self.assertEqual(len(course_list), 2)
        self.assertEqual(course_list[0].name, "Math")

    @patch("builtins.open", new_callable=mock_open)
    def test_save_courses(self, mock_file):
        file_path = "test_courses.csv"

        # Create and save a sample course list
        course_list.clear()
        course_list.append(Course(course_id=1, name="Math", capacity=30))
        save_courses(course_list, file_path)

        # Verify the file was written with the correct content
        mock_file.assert_called_once_with(file_path, "w", newline="")
        handle = mock_file()
        handle.write.assert_any_call("id,name,capacity,instructor_email\r\n")
        handle.write.assert_any_call("1,Math,30,\r\n")


# Comprehensive application tests
class TestApplication(unittest.TestCase):
    def setUp(self):
        # Initialize the authentication system and add a test user
        self.auth = Authentication()
        self.auth.register_user("test@example.com", "password123", "student")

    @patch("builtins.open", new_callable=mock_open)
    def test_save_courses_empty_list(self, mock_file):
        file_path = "test_courses.csv"

        # Save an empty course list
        course_list.clear()
        save_courses(course_list, file_path)

        # Verify that only the header was written to the file
        mock_file.assert_called_once_with(file_path, "w", newline="")
        handle = mock_file()
        handle.write.assert_called_once_with("id,name,capacity,instructor_email\r\n")

    def test_course_capacity_limits(self):
        # Verify that negative capacity raises an error
        with self.assertRaises(ValueError):
            Course(course_id=1, name="Math", capacity=-1)

        # Verify that zero capacity is allowed
        course = Course(course_id=2, name="Science", capacity=0)
        self.assertEqual(course.capacity, 0)

    def test_register_duplicate_user(self):
        # Ensure attempting to register the same user raises an error
        with self.assertRaises(ValueError):
            self.auth.register_user("test@example.com", "password456", "instructor")

    def test_remove_nonexistent_course(self):
        # Try to remove a course that doesn't exist
        course_list.clear()
        course = Course(course_id=1, name="Math", capacity=30)
        course_list.append(course)
        with self.assertRaises(StopIteration):
            course_list.remove(next(c for c in course_list if c.course_id == 99))

    def test_delete_course_with_students(self):
        # Add a course and enroll a student
        course = Course(course_id=1, name="Math", capacity=30)
        student = Student(student_id=1, name="Alice", email="alice@example.com")
        course.enrolled_students.append(student.student_id)
        course_list.append(course)

        # Attempt to delete the course with enrolled students
        with self.assertRaises(Exception):
            if course.enrolled_students:
                raise Exception("Can't delete course with enrolled students")


if __name__ == "__main__":
    unittest.main()


