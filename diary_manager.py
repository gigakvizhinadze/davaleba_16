import json
import os

class DiaryManager:
    def __init__(self, user):
        self.user = user
        self.entries = []

    def load_entries(self):
        try:
            with open(f"{self.user}_diary.json", 'r') as file:
                self.entries = json.load(file)
        except FileNotFoundError:
            self.entries = []

    def save_entries(self):
        with open(f"{self.user}_diary.json", 'w') as file:
            json.dump(self.entries, file)

    def add_entry(self, memo):
        self.entries.append(memo)

    def delete_entry(self, index):
        if 0 <= index < len(self.entries):
            del self.entries[index]
            return True
        else:
            return False

    def get_entries(self):
        return self.entries
