import sqlite3
from pathlib import Path
import pandas as pd

# Paths relative to project root
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "movies.db"

# Step 1: Connect to Database Helper
def get_connection():
    """Create and return a connection to the SQLite database."""
    return sqlite3.connect(DB_PATH)

# Step 2: Define Query Functions
def top_10_highest_rated_after_2000(connection=None):
    """Return top 10 highest-rated movies released after 2000."""
    close_after = False
    if connection is None:
        connection = get_connection()
        close_after = True

    query = """
    SELECT title, genre, release_year, rating
    FROM movies
    WHERE release_year > 2000
    ORDER BY rating DESC
    LIMIT 10;
    """
    df = pd.read_sql_query(query, connection)
    if close_after:
        connection.close()
    return df

def average_rating_by_genre(connection=None):
    """Return average rating grouped by genre."""
    close_after = False
    if connection is None:
        connection = get_connection()
        close_after = True

    query = """
    SELECT genre, ROUND(AVG(rating), 2) AS avg_rating
    FROM movies
    GROUP BY genre
    ORDER BY avg_rating DESC;
    """
    df = pd.read_sql_query(query, connection)
    if close_after:
        connection.close()
    return df

def top_5_highest_revenue_movies(connection=None):
    """Return top 5 movies with highest revenue."""
    close_after = False
    if connection is None:
        connection = get_connection()
        close_after = True

    query = """
    SELECT title, genre, release_year, revenue
    FROM movies
    ORDER BY revenue DESC
    LIMIT 5;
    """
    df = pd.read_sql_query(query, connection)
    if close_after:
        connection.close()
    return df

def movies_with_rating_above_8(connection=None):
    """Return movies with rating above 8."""
    close_after = False
    if connection is None:
        connection = get_connection()
        close_after = True

    query = """
    SELECT title, genre, release_year, rating
    FROM movies
    WHERE rating > 8
    ORDER BY rating DESC;
    """
    df = pd.read_sql_query(query, connection)
    if close_after:
        connection.close()
    return df

def movies_per_decade(connection=None):
    """Return number of movies released per decade."""
    close_after = False
    if connection is None:
        connection = get_connection()
        close_after = True

    query = """
    SELECT (release_year/10)*10 AS decade, COUNT(*) AS movie_count
    FROM movies
    GROUP BY decade
    ORDER BY decade;
    """
    df = pd.read_sql_query(query, connection)
    if close_after:
        connection.close()
    return df

# Step 3: Test Queries
if __name__ == "__main__":
    conn = get_connection()
    try:
        print("\nTop 10 Highest Rated Movies After 2000")
        print(top_10_highest_rated_after_2000(conn))

        print("\nAverage Rating by Genre")
        print(average_rating_by_genre(conn))

        print("\nTop 5 Highest Revenue Movies")
        print(top_5_highest_revenue_movies(conn))

        print("\nMovies with Rating Above 8")
        print(movies_with_rating_above_8(conn))

        print("\nNumber of Movies Released per Decade")
        print(movies_per_decade(conn))
    finally:
        conn.close()
