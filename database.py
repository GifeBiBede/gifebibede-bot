import sqlite3
from config import DATABASE_NAME

def get_connection():
    return sqlite3.connect(DATABASE_NAME)


def create_tables():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS gifs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        code TEXT UNIQUE NOT NULL,
        file_id TEXT NOT NULL,
        file_type TEXT DEFAULT 'animation',
        downloads INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

    conn.commit()
    conn.close()


def add_gif(code, file_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO gifs(code,file_id) VALUES(?,?)",
        (code, file_id)
    )

    conn.commit()
    conn.close()


def get_gif(code):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT file_id FROM gifs WHERE code=?",
        (code,)
    )

    result = cur.fetchone()

    conn.close()

    return result


def increase_download(code):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "UPDATE gifs SET downloads=downloads+1 WHERE code=?",
        (code,)
    )

    conn.commit()
    conn.close()


def delete_gif(code):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM gifs WHERE code=?",
        (code,)
    )

    conn.commit()
    conn.close()


def list_gifs():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT code,downloads FROM gifs ORDER BY id DESC"
    )

    data = cur.fetchall()

    conn.close()

    return data
