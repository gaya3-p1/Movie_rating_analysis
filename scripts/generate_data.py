import random
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
CSV_PATH = BASE_DIR / "data" / "movies.csv"
CSV_PATH.parent.mkdir(parents=True, exist_ok=True)

genres = ["Action", "Comedy", "Drama", "Horror", "Romance", "Sci-Fi", "Thriller", "Animation"]
titles_prefix = ["The", "A", "Return of", "Rise of", "Battle for", "Journey to", "Escape from", "Legend of"]
titles_suffix = ["Future", "Love", "Warrior", "Dreams", "Galaxy", "Secrets", "Night", "Destiny"]

random.seed(42)

movies = []
for movie_id in range(1, 246):
    title = f"{random.choice(titles_prefix)} {random.choice(titles_suffix)}"
    genre = random.choice(genres)
    release_year = random.randint(1980, 2025)
    rating = round(random.uniform(1.0, 10.0), 1)

    if random.random() < 0.05:
        revenue = None
    else:
        revenue = round(random.uniform(1e6, 500e6), 2)

    movies.append([movie_id, title, genre, release_year, rating, revenue])

movies.append([246, "Legend of Outlier", "Action", 2021, -1.5, 150000000.00])
movies.append([247, "Rise of Masterpiece", "Drama", 2023, 11.2, 280000000.00])

movies.append([248, movies[10][1], movies[10][2], movies[10][3], movies[10][4], movies[10][5]])
movies.append([249, movies[25][1], movies[25][2], movies[25][3], movies[25][4], movies[25][5]])
movies.append([250, movies[50][1], movies[50][2], movies[50][3], movies[50][4], movies[50][5]])

df = pd.DataFrame(movies, columns=["movie_id", "title", "genre", "release_year", "rating", "revenue"])

df.to_csv(CSV_PATH, index=False)

print(f"Generated {len(df)} movies in {CSV_PATH} (including missing revenue, duplicate titles, and outlier ratings).")
