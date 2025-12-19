import sqlite3
import os

import tempfile

# Determine DB path based on environment
# Vercel file system is read-only except for /tmp
try:
    with open('test_write', 'w') as f: f.write('test')
    os.remove('test_write')
    DB_NAME = 'anxiety_screen.db'
except OSError:
    DB_NAME = os.path.join(tempfile.gettempdir(), 'anxiety_screen.db')

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    if not os.path.exists(DB_NAME):
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Create Students Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_hash TEXT NOT NULL,
                age INTEGER,
                gender TEXT,
                score INTEGER,
                classification TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Create Doctors Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS doctors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                specialization TEXT,
                phone TEXT,
                location TEXT
            )
        ''')
        
        # Insert Dummy Doctors
        doctors = [
            ('Dr. Ayesha Khan', 'Clinical Psychologist', '01711-111111', 'Dhaka'),
            ('Dr. Rafiqul Islam', 'Psychiatrist', '01822-222222', 'Chittagong'),
            ('Dr. Sarah Ahmed', 'Counselor', '01933-333333', 'Sylhet')
        ]
        
        cursor.executemany('INSERT INTO doctors (name, specialization, phone, location) VALUES (?, ?, ?, ?)', doctors)
        
        conn.commit()
        conn.close()
        print(f"Database {DB_NAME} initialized with dummy data.")
    else:
        print(f"Database {DB_NAME} already exists.")

if __name__ == '__main__':
    init_db()
