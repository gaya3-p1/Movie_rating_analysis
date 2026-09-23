import sqlite3
from pathlib import Path
import pandas as pd
import numpy as np

# Paths relative to project root
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "movies.db"
CLEANED_CSV_PATH = BASE_DIR / "data" / "movies_cleaned.csv"

# Step 1: Load Data from SQLite
connection = sqlite3.connect(DB_PATH)
df = pd.read_sql_query("SELECT * FROM movies", connection)

print("Loaded data from database")
print(f"Rows before cleaning: {len(df)}")

# Step 2: Check for Missing Values
print("\n🔍 Missing values per column:")
print(df.isnull().sum())

# Step 3: Remove Duplicate Records
# Deduplicate based on movie title and release year
df.drop_duplicates(subset=['title', 'release_year'], keep='first', inplace=True)
print(f"\nRemoved duplicates. Rows now: {len(df)}")

# Step 4: Handle Missing Revenue
# Replace missing revenue values with the median revenue
median_revenue = df['revenue'].median()
df['revenue'] = df['revenue'].fillna(median_revenue)
print(f"\nMissing revenue values replaced with median (${median_revenue:,.2f})")

# Step 5: Ensure Ratings Between 0 and 10
# rating < 0 → 0
# rating > 10 → 10
df['rating'] = df['rating'].clip(lower=0, upper=10)
print("Ratings adjusted to be between 0 and 10")

# Step 6: Save Cleaned Data
# Retain original SQLite schema and primary key constraints
cursor = connection.cursor()
cursor.execute("DELETE FROM movies")
cursor.executemany("""
INSERT INTO movies (movie_id, title, genre, release_year, rating, revenue)
VALUES (?, ?, ?, ?, ?, ?)
""", df.where(pd.notnull(df), None).values.tolist())

# Saving a cleaned CSV for reference
CLEANED_CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(CLEANED_CSV_PATH, index=False)

print("\nData cleaning complete!")
print(f"Rows after cleaning: {len(df)}")

connection.commit()
connection.close()
