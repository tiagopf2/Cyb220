# Written by Tiago Perez

# 9.7 Admin

class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("Administrator Privileges:")
        for privilege in self.privileges:
            print(privilege)


class User:
    def __init__(self, first_name, last_name, username, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.location = location

    def describe_user(self):
        print("User Information:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")


class Admin(User):
    def __init__(self, first_name, last_name, username, location, privileges):
        super().__init__(first_name, last_name, username, location)
        self.privileges = Privileges(privileges)
