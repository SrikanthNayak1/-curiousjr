import sqlite3

def create_db():
    conn = sqlite3.connect('curiousjr.db')
    cursor = conn.cursor()

    # Create users table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL,
                        password TEXT NOT NULL,
                        badges TEXT DEFAULT '',
                        total_points INTEGER DEFAULT 0)''')

    # Create progress table
    cursor.execute('''CREATE TABLE IF NOT EXISTS progress (
                        user_id INTEGER,
                        course_name TEXT NOT NULL,
                        progress INTEGER DEFAULT 0,
                        FOREIGN KEY (user_id) REFERENCES users(id))''')

    conn.commit()
    conn.close()
