import sqlite3
from pathlib import Path
import pandas as pd

# Paths relative to project root
BASE_DIR = Path(__file__).resolve().parent.parent
CSV_PATH = BASE_DIR / "data" / "movies.csv"
DB_PATH = BASE_DIR / "database" / "movies.db"

if not CSV_PATH.exists():
    raise FileNotFoundError(f"Source file {CSV_PATH} not found. Please run generate_data.py first.")

# Step 1: Load CSV with Pandas
df = pd.read_csv(CSV_PATH)

print("Loaded movies.csv successfully!")
print(f"Total rows in CSV: {len(df)}")

# Step 2: Connect to SQLite DB
connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

# Step 3: Insert Data into DB
cursor.executemany("""
INSERT OR REPLACE INTO movies (movie_id, title, genre, release_year, rating, revenue)
VALUES (?, ?, ?, ?, ?, ?)
""", df.where(pd.notnull(df), None).values.tolist())

print("Data imported into movies.db successfully!!")

# Step 4: Verify Import
cursor.execute("SELECT COUNT(*) FROM movies")
row_count = cursor.fetchone()[0]
print(f"Total rows in database: {row_count}")

connection.commit()
connection.close()
