import sqlite3
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Paths relative to project root
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "movies.db"
OUTPUT_DIR = BASE_DIR / "plots"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Step 1: Load Data from SQLite
connection = sqlite3.connect(DB_PATH)
df = pd.read_sql_query("SELECT * FROM movies", connection)
connection.close()

print(f"Data loaded for visualization: {len(df)} records")

# Step 2: Histogram of Ratings
plt.figure(figsize=(8, 6))
sns.histplot(df['rating'], bins=20, kde=True, color="skyblue")
plt.title("Distribution of Movie Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Movies")
plt.grid(True)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "rating_distribution.png")
print(f"Saved: {OUTPUT_DIR / 'rating_distribution.png'}")
plt.close()

# Step 3: Bar Chart of Genre Ratings
avg_genre_rating = df.groupby("genre")["rating"].mean().sort_values()
plt.figure(figsize=(10, 6))
sns.barplot(
    x=avg_genre_rating.index,
    y=avg_genre_rating.values,
    hue=avg_genre_rating.index,
    palette="viridis",
    legend=False
)
plt.title("Average Rating by Genre")
plt.xlabel("Genre")
plt.ylabel("Average Rating")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "genre_ratings.png")
print(f"Saved: {OUTPUT_DIR / 'genre_ratings.png'}")
plt.close()

# Step 4: Line Chart of Revenue Trends
avg_revenue_year = df.groupby("release_year")["revenue"].mean()
plt.figure(figsize=(10, 6))
sns.lineplot(x=avg_revenue_year.index, y=avg_revenue_year.values, marker="o", color="red")
plt.title("Average Revenue Trend Over Years")
plt.xlabel("Release Year")
plt.ylabel("Average Revenue ($)")
plt.grid(True)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "revenue_trends.png")
print(f"Saved: {OUTPUT_DIR / 'revenue_trends.png'}")
plt.close()

# Step 5: Scatter Plot Rating vs Revenue
plt.figure(figsize=(8, 6))
sns.scatterplot(x="rating", y="revenue", data=df, hue="genre", palette="Set2")
plt.title("Rating vs Revenue")
plt.xlabel("Rating")
plt.ylabel("Revenue ($)")
plt.grid(True)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "rating_vs_revenue.png")
print(f"Saved: {OUTPUT_DIR / 'rating_vs_revenue.png'}")
plt.close()

# Step 6: Correlation Heatmap
plt.figure(figsize=(6, 4))
corr = df[["rating", "revenue", "release_year"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "correlation_heatmap.png")
print(f"Saved: {OUTPUT_DIR / 'correlation_heatmap.png'}")
plt.close()

print("\nAll visualizations generated and saved successfully!")
