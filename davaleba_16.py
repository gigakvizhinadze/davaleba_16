from user_manager import UserManager
from diary_manager import DiaryManager

def main():
    user_manager = UserManager()
    user_manager.load_users()

    while True:
        print("\nWelcome to the JSON Diary App!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if user_manager.register_user(username, password):
                print("User registered successfully.")
            else:
                print("Username already exists.")

        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if user_manager.login_user(username, password):
                print("Login successful.")
                diary_manager = DiaryManager(username)
                diary_manager.load_entries()
                diary_menu(diary_manager)
            else:
                print("Invalid username or password.")

        elif choice == '3':
            break

        else:
            print("Invalid choice. Please try again.")

def diary_menu(diary_manager):
    while True:
        print("\nDiary Menu:")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Delete Entry")
        print("4. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            memo = input("Enter memo: ")
            diary_manager.add_entry(memo)
            diary_manager.save_entries()
            print("Entry added successfully.")

        elif choice == '2':
            entries = diary_manager.get_entries()
            print("\nDiary Entries:")
            for index, entry in enumerate(entries, start=1):
                print(f"{index}. {entry}")

        elif choice == '3':
            index = int(input("Enter the index of the memo to delete: ")) - 1
            if diary_manager.delete_entry(index):
                diary_manager.save_entries()
                print("Entry deleted successfully.")
            else:
                print("Invalid index.")

        elif choice == '4':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
