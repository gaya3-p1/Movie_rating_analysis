import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "movies.db"

DB_PATH.parent.mkdir(parents=True, exist_ok=True)

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS movies (
    movie_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    genre TEXT NOT NULL,
    release_year INTEGER NOT NULL,
    rating REAL NOT NULL,
    revenue REAL
);
""")

print("Movies table created successfully!!!!")

connection.commit()
connection.close()
