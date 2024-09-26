import sqlite3

def show_courses():
    courses = ["Loops in Python", "Variables and Data Types", "Functions in Python"]
    for index, course in enumerate(courses):
        print(f"{index + 1}. {course}")
    course_choice = int(input("Choose a course number to start: ")) - 1
    selected_course = courses[course_choice]
    return selected_course

def update_course_progress(user_id, course_name):
    conn = sqlite3.connect('curiousjr.db')
    cursor = conn.cursor()

    # Check if progress exists
    cursor.execute("SELECT progress FROM progress WHERE user_id = ? AND course_name = ?", (user_id, course_name))
    progress = cursor.fetchone()

    if not progress:
        cursor.execute("INSERT INTO progress (user_id, course_name, progress) VALUES (?, ?, ?)", (user_id, course_name, 0))
    
    # Update progress
    cursor.execute("UPDATE progress SET progress = progress + 20 WHERE user_id = ? AND course_name = ?", (user_id, course_name))
    conn.commit()
    print(f"Progress for {course_name} updated!")
    conn.close()
