class Admin:
    def __init__(self, email):
        self.email = email

    def __str__(self):
        return f"Admin Email: {self.email}"
