import sqlite3
from datetime import datetime

DB_PATH = "database/smart_ats.db"


def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resumes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        email TEXT,
        filename TEXT,
        upload_date TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS feedback(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        score REAL,
        matched_skills TEXT,
        missing_skills TEXT,
        report_path TEXT
    )
    """)

    conn.commit()
    conn.close()


# ---------------- USER FUNCTIONS ---------------- #

def add_user(username, password, role):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users(username,password,role) VALUES(?,?,?)",
            (username, password, role)
        )
        conn.commit()
        return True

    except:
        return False

    finally:
        conn.close()


def get_user(username):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=?",
        (username,)
    )

    user = cursor.fetchone()

    conn.close()

    return user


# ---------------- RESUME FUNCTIONS ---------------- #

def save_resume(username, email, filename):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO resumes(username,email,filename,upload_date)
        VALUES(?,?,?,?)
        """,
        (
            username,
            email,
            filename,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
    )

    conn.commit()
    conn.close()


def get_all_resumes():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM resumes")

    data = cursor.fetchall()

    conn.close()

    return data


# ---------------- FEEDBACK FUNCTIONS ---------------- #

def save_feedback(
        username,
        score,
        matched_skills,
        missing_skills,
        report_path):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO feedback
        (username,score,matched_skills,missing_skills,report_path)
        VALUES(?,?,?,?,?)
        """,
        (
            username,
            score,
            matched_skills,
            missing_skills,
            report_path
        )
    )

    conn.commit()
    conn.close()


def get_feedback():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM feedback")

    data = cursor.fetchall()

    conn.close()

    return data