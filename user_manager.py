import json

class UserManager:
    def __init__(self):
        self.users = {}

    def load_users(self):
        try:
            with open('users.json', 'r') as file:
                self.users = json.load(file)
        except FileNotFoundError:
            self.users = {}

    def save_users(self):
        with open('users.json', 'w') as file:
            json.dump(self.users, file)

    def register_user(self, username, password):
        if username in self.users:
            return False  # Username already exists
        self.users[username] = password
        self.save_users()
        return True

    def login_user(self, username, password):
        return self.users.get(username) == password
