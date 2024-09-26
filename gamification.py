import sqlite3

def award_badges(user_id, progress):
    conn = sqlite3.connect('curiousjr.db')
    cursor = conn.cursor()
    
    if progress >= 100:
        cursor.execute("UPDATE users SET badges = 'Python Beginner', total_points = total_points + 50 WHERE id = ?", (user_id,))
        print("Congratulations! You've earned the Python Beginner badge and 50 points!")
        
    conn.commit()
    conn.close()

def show_leaderboard():
    conn = sqlite3.connect('curiousjr.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT username, total_points FROM users ORDER BY total_points DESC")
    leaderboard = cursor.fetchall()
    
    print("Leaderboard:")
    for rank, (username, points) in enumerate(leaderboard, start=1):
        print(f"{rank}. {username} - {points} points")
    
    conn.close()
