import sqlite3
import os

DB_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'hms_database.db')

def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row  # This allows accessing columns by name like a dictionary
    return conn

def execute_query(query, params=None, fetch=False):
    """
    Utility function to execute a query using SQLite.
    """
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params or ())
            
            if fetch:
                # Convert sqlite3.Row objects to standard dictionaries for compatibility
                return [dict(row) for row in cursor.fetchall()]
            
            conn.commit()
            return cursor.lastrowid
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        raise

def initialize_database():
    """Creates the necessary tables if they don't exist and inserts default admin."""
    tables = [
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT DEFAULT 'receptionist',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            gender TEXT,
            contact_number TEXT,
            address TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS doctors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            specialty TEXT,
            contact_number TEXT,
            availability TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER,
            doctor_id INTEGER,
            appointment_date TEXT NOT NULL,
            appointment_time TEXT NOT NULL,
            status TEXT DEFAULT 'Scheduled',
            FOREIGN KEY (patient_id) REFERENCES patients(id) ON DELETE CASCADE,
            FOREIGN KEY (doctor_id) REFERENCES doctors(id) ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS medical_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER,
            doctor_id INTEGER,
            diagnosis TEXT,
            prescription TEXT,
            notes TEXT,
            record_date TEXT NOT NULL,
            FOREIGN KEY (patient_id) REFERENCES patients(id) ON DELETE CASCADE,
            FOREIGN KEY (doctor_id) REFERENCES doctors(id) ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS billing (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER,
            amount REAL NOT NULL,
            status TEXT DEFAULT 'Unpaid',
            billing_date TEXT NOT NULL,
            FOREIGN KEY (patient_id) REFERENCES patients(id) ON DELETE CASCADE
        )
        """
    ]
    
    for table_sql in tables:
        execute_query(table_sql)
        
    # Insert default admin if no users exist
    try:
        users = execute_query("SELECT COUNT(*) as count FROM users", fetch=True)
        if users[0]['count'] == 0:
            execute_query("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", 
                          ('admin', 'admin123', 'admin'))
    except Exception as e:
        print(f"Error inserting admin: {e}")

# Automatically initialize DB when this module is imported
initialize_database()
