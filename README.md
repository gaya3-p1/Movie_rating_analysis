# Movie Rating Analysis

An end-to-end Python and SQLite data analysis project exploring movie ratings, genres, release years, and box-office revenue trends.

---

## Project Structure

```text
Movie_rating_analysis/
├── data/
│   ├── movies.csv             # Raw dataset (200 sample movies)
│   └── movies_cleaned.csv     # Cleaned dataset after preprocessing
├── database/
│   └── movies.db              # SQLite database storing movie records
├── notebooks/
│   └── movie_analysis.ipynb   # Interactive EDA notebook with charts
├── plots/
│   ├── correlation_heatmap.png
│   ├── genre_ratings.png
│   ├── rating_distribution.png
│   ├── rating_vs_revenue.png
│   └── revenue_trends.png
├── scripts/
│   ├── generate_data.py       # Generates synthetic movies dataset
│   ├── create_database.py     # Initializes the SQLite database schema
│   ├── import_data.py         # Imports movies.csv into movies.db
│   ├── data_cleaning.py       # Cleans missing values, bounds ratings, deduplicates
│   ├── sql_queries.py         # Runs analytical SQL queries
│   └── visualization.py       # Generates and saves visual charts
├── requirements.txt           # Project dependencies
└── README.md                  # Documentation
```

---

## Getting Started

### 1. Install Dependencies

Ensure Python 3.10+ is installed, then install required packages:

```bash
make install
# or: pip install -r requirements.txt
```

### 2. Run the Pipeline

You can run the entire pipeline with a single command:

```bash
make pipeline
```

Or execute individual steps using `make` or Python:

```bash
make generate-data   # 1. Generate the synthetic dataset
make init-db         # 2. Initialize the SQLite database schema
make import-data     # 3. Import raw data into the SQLite database
make clean-data      # 4. Clean data (impute missing revenue, bound ratings, deduplicate)
make queries         # 5. Run analytical SQL queries
make visualize       # 6. Generate and save visualization figures to plots/
```

```bash
# 1. Generate the synthetic dataset
python scripts/generate_data.py

# 2. Initialize the SQLite database schema
python scripts/create_database.py

# 3. Import raw data into the SQLite database
python scripts/import_data.py

# 4. Clean data (impute missing revenue with median, bound ratings, deduplicate)
python scripts/data_cleaning.py

# 5. Run analytical SQL queries
python scripts/sql_queries.py

# 6. Generate and save visualization figures to plots/
python scripts/visualization.py
```

### 3. Interactive Notebook

To explore the data interactively:

```bash
jupyter notebook notebooks/movie_analysis.ipynb
```

---

## Analytical Insights

- **Top 10 Highest Rated Movies (post-2000)**
- **Average Rating by Genre**
- **Top 5 Highest Revenue Movies**
- **Movies Rated Above 8.0**
- **Decade-by-Decade Movie Release Counts**
- **Visual Plots:** Rating distribution, average genre rating, revenue trends over time, rating vs. revenue correlation, and metric heatmap.
