class Admin:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"Admin Name: {self.name}, Email: {self.email}"
