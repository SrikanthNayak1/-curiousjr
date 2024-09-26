import sqlite3
from database import create_db
from courses import show_courses, update_course_progress
from gamification import award_badges, show_leaderboard

def register():
    conn = sqlite3.connect('curiousjr.db')
    cursor = conn.cursor()
    
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    print("Registration successful!")
    conn.close()

def login():
    conn = sqlite3.connect('curiousjr.db')
    cursor = conn.cursor()
    
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    
    if user:
        print("Login successful!")
        return user[0]  # Return user_id
    else:
        print("Login failed!")
        return None

def main():
    create_db()  # Ensure the database is created when running the script
    print("Welcome to the CuriousJr App")
    
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            register()
        elif choice == '2':
            user_id = login()
            if user_id:
                while True:
                    print("\n1. Show Courses")
                    print("2. Update Course Progress")
                    print("3. Award Badges")
                    print("4. Show Leaderboard")
                    print("5. Logout")
                    
                    action = input("Choose an action: ")
                    
                    if action == '1':
                        selected_course = show_courses()
                        update_course_progress(user_id, selected_course)
                    elif action == '2':
                        selected_course = show_courses()
                        update_course_progress(user_id, selected_course)
                    elif action == '3':
                        # Assume the user has made progress, e.g., 100
                        award_badges(user_id, 100)  # Replace 100 with actual progress
                    elif action == '4':
                        show_leaderboard()
                    elif action == '5':
                        print("Logged out.")
                        break
                    else:
                        print("Invalid option, please try again.")
        elif choice == '3':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
