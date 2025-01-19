import hashlib
import csv

class Authentication:
    def __init__(self, database_path="users.csv"):
        self.database = database_path
        self.users = {}  # Память для хранения пользователей

        try:
            print(f"Loading users from {self.database}...")
            with open(self.database, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.users[row["email"]] = {
                        "password": row["password"],
                        "role": row["role"]
                    }
            print(f"Loaded users: {self.users}")
        except FileNotFoundError:
            print(f"Database file '{self.database}' not found. Starting fresh.")
        except Exception as e:
            print(f"Error loading users: {e}")


        self.database = database_path  # Устанавливаем путь к базе данных

    def register_user(self, email, password, role):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if email in self.users:
            print(f"User '{email}' already exists in memory!")
            return

        self.users[email] = {"password": hashed_password, "role": role}  # Сохраняем в память

        # Запись в CSV
        try:
            print(f"Saving user to CSV: email={email}, role={role}")
            with open(self.database, "a", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["email", "password", "role"])
                writer.writerow({"email": email, "password": hashed_password, "role": role})
        except Exception as e:
            print(f"Error writing user to CSV: {e}")



    def login_user(self, email, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        user = self.users.get(email)
        if not user:
            print(f"User '{email}' not found in memory.")
            return None

        if user["password"] == hashed_password:
            print(f"Login successful for user '{email}' with role '{user['role']}'.")
            return user["role"]
        else:
            print(f"Invalid password for user '{email}'.")
            return None

