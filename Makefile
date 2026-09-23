# Variables
PYTHON ?= python3
PIP ?= $(PYTHON) -m pip

.PHONY: help install pipeline all run generate-data init-db import-data clean-data queries visualize notebook clean

# Default target: display help
help:
	@echo "================================================================"
	@echo " Movie Rating Analysis - Makefile Commands"
	@echo "================================================================"
	@echo "  make install        Install required Python dependencies"
	@echo "  make pipeline       Run full pipeline end-to-end"
	@echo "  make generate-data  Generate synthetic movies dataset"
	@echo "  make init-db        Create database and table schema"
	@echo "  make import-data    Import movies.csv into SQLite database"
	@echo "  make clean-data     Clean records and export movies_cleaned.csv"
	@echo "  make queries        Execute analytical SQL queries"
	@echo "  make visualize      Generate and save visual plots to plots/"
	@echo "  make notebook       Launch Jupyter notebook"
	@echo "  make clean          Remove generated database, cleaned data, and plots"
	@echo "================================================================"

# Install project dependencies
install:
	$(PIP) install -r requirements.txt

# Run complete end-to-end pipeline
pipeline: generate-data init-db import-data clean-data queries visualize
	@echo "Pipeline execution completed successfully!"

all: pipeline
run: pipeline

# Step 1: Generate synthetic movies dataset
generate-data:
	$(PYTHON) scripts/generate_data.py

# Step 2: Initialize SQLite database and tables
init-db:
	$(PYTHON) scripts/create_database.py

# Step 3: Import raw movies.csv into SQLite database
import-data:
	$(PYTHON) scripts/import_data.py

# Step 4: Clean data and export cleaned CSV
clean-data:
	$(PYTHON) scripts/data_cleaning.py

# Step 5: Execute analytical SQL queries
queries:
	$(PYTHON) scripts/sql_queries.py

# Step 6: Generate and save visualization plots
visualize:
	$(PYTHON) scripts/visualization.py

# Launch interactive EDA notebook
notebook:
	jupyter notebook notebooks/movie_analysis.ipynb

# Clean generated artifacts and caches
clean:
	rm -f database/movies.db
	rm -f data/movies_cleaned.csv
	rm -f plots/*.png
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} +
	@echo "Cleaned generated files and caches."
