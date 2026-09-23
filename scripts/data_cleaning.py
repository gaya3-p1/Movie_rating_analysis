import sqlite3
from pathlib import Path
import pandas as pd
import numpy as np

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "movies.db"
CLEANED_CSV_PATH = BASE_DIR / "data" / "movies_cleaned.csv"

connection = sqlite3.connect(DB_PATH)
df = pd.read_sql_query("SELECT * FROM movies", connection)

print("Loaded data from database")
print(f"Rows before cleaning: {len(df)}")

print("\n🔍 Missing values per column:")
print(df.isnull().sum())

df.drop_duplicates(subset=['title', 'release_year'], keep='first', inplace=True)
print(f"\nRemoved duplicates. Rows now: {len(df)}")

median_revenue = df['revenue'].median()
df['revenue'] = df['revenue'].fillna(median_revenue)
print(f"\nMissing revenue values replaced with median (${median_revenue:,.2f})")

df['rating'] = df['rating'].clip(lower=0, upper=10)
print("Ratings adjusted to be between 0 and 10")

cursor = connection.cursor()
cursor.execute("DELETE FROM movies")
cursor.executemany("""
INSERT INTO movies (movie_id, title, genre, release_year, rating, revenue)
VALUES (?, ?, ?, ?, ?, ?)
""", df.where(pd.notnull(df), None).values.tolist())

CLEANED_CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(CLEANED_CSV_PATH, index=False)

print("\nData cleaning complete!")
print(f"Rows after cleaning: {len(df)}")

connection.commit()
connection.close()
