import sqlite3
import datetime

conn = sqlite3.connect('songlist.db')

print ("Opened database successfully")

conn.execute('''
CREATE TABLE IF NOT EXISTS songlist(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    requester TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
             
);
''')
             
def get_songs_last_day(conn):
    cur = conn.cursor()
    date = datetime.date.today()
    formatted = f"{date}%"
    cur.execute("SELECT * FROM songlist WHERE timestamp LIKE ?", (formatted,))
    results = cur.fetchall()  

    return results

def get_latest_songs(conn, amount):
    cur = conn.cursor()
    cur.execute("SELECT * FROM songlist ORDER BY timestamp DESC LIMIT ?", (amount,))
    result = cur.fetchall()

    return result