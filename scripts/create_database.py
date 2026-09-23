import sqlite3
from pathlib import Path

# Paths relative to project root
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "movies.db"

# Ensure database directory exists
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

# Step 1: Connect to SQLite DB
connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

# Step 2: Create Movies Table
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

# Step 3: Close Connection
connection.commit()
connection.close()
