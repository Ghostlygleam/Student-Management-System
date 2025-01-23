import hashlib
import csv


class Authentication:
    def __init__(self, database_path="users.csv"):
        self.database = database_path
        self.users = {}

        # Load existing users from CSV
        try:
            print(f"Checking for user database: {self.database}")
            with open(self.database, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if "email" in row and "password" in row and "role" in row:
                        self.users[row["email"]] = {
                            "password": row["password"],
                            "role": row["role"]
                        }
                print(f"Successfully loaded {len(self.users)} user(s).")
        except FileNotFoundError:
            print(f"Warning: No database found at '{self.database}'. Starting with an empty user list.")
        except Exception as e:
            print(f"Unexpected error while loading users: {e}")

    def register_user(self, email, password, role):
        if email in self.users:
            print(f"Cannot register '{email}': User already exists.")
            return
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        self.users[email] = {"password": hashed_password, "role": role}

        try:
            print(f"Adding new user: {email} as '{role}'")
            with open(self.database, "a", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["email", "password", "role"])
                if file.tell() == 0:  # Write header if file is empty
                    writer.writeheader()
                writer.writerow({"email": email, "password": hashed_password, "role": role})
            print(f"User '{email}' registered successfully and saved to the database.")
        except FileNotFoundError:
            print(f"Error: Cannot save '{email}' - database file not found.")
        except PermissionError:
            print(f"Error: Insufficient permissions to write to '{self.database}'.")
        except Exception as e:
            print(f"Unexpected error while saving user '{email}': {e}")

    def login_user(self, email, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        user = self.users.get(email)

        if not user:
            print(f"Access denied: No user found with email '{email}'.")
            return None

        if user["password"] == hashed_password:
            print(f"Welcome back, {email}! Your role is '{user['role']}'.")
            return user["role"]
        else:
            print(f"Login failed: Incorrect password for '{email}'.")
            return None
