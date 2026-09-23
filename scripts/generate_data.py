import random
from pathlib import Path
import pandas as pd

# Define paths relative to repository root
BASE_DIR = Path(__file__).resolve().parent.parent
CSV_PATH = BASE_DIR / "data" / "movies.csv"
CSV_PATH.parent.mkdir(parents=True, exist_ok=True)

# Step 1: Define Genres & Titles
genres = ["Action", "Comedy", "Drama", "Horror", "Romance", "Sci-Fi", "Thriller", "Animation"]
titles_prefix = ["The", "A", "Return of", "Rise of", "Battle for", "Journey to", "Escape from", "Legend of"]
titles_suffix = ["Future", "Love", "Warrior", "Dreams", "Galaxy", "Secrets", "Night", "Destiny"]

# Set random seed for reproducibility
random.seed(42)

# Step 2: Generate 250 Movies with realistic data anomalies
movies = []
for movie_id in range(1, 246):  # 245 base movies
    title = f"{random.choice(titles_prefix)} {random.choice(titles_suffix)}"
    genre = random.choice(genres)
    release_year = random.randint(1980, 2025)
    rating = round(random.uniform(1.0, 10.0), 1)

    # Introduce ~5% missing revenue (simulating unrecorded box office)
    if random.random() < 0.05:
        revenue = None
    else:
        revenue = round(random.uniform(1e6, 500e6), 2)

    movies.append([movie_id, title, genre, release_year, rating, revenue])

# Add 2 movies with out-of-range ratings (data entry errors to test clipping)
movies.append([246, "Legend of Outlier", "Action", 2021, -1.5, 150000000.00])
movies.append([247, "Rise of Masterpiece", "Drama", 2023, 11.2, 280000000.00])

# Add 3 duplicate movies with duplicate title and release_year under new IDs
movies.append([248, movies[10][1], movies[10][2], movies[10][3], movies[10][4], movies[10][5]])
movies.append([249, movies[25][1], movies[25][2], movies[25][3], movies[25][4], movies[25][5]])
movies.append([250, movies[50][1], movies[50][2], movies[50][3], movies[50][4], movies[50][5]])

# Step 3: Create DataFrame
df = pd.DataFrame(movies, columns=["movie_id", "title", "genre", "release_year", "rating", "revenue"])

# Step 4: Save to CSV
df.to_csv(CSV_PATH, index=False)

print(f"Generated {len(df)} movies in {CSV_PATH} (including missing revenue, duplicate titles, and outlier ratings).")
