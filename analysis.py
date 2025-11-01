"""
CSE 310 - Module 1: Data Analysis
Author: Michael Akpan
Date: November 1, 2025
Selected Module: Data Analysis

Description:
This program analyzes the Netflix Titles dataset from Kaggle to answer three questions:
1. Which countries produce the most Netflix titles?
2. What is the average release year of Movies vs. TV Shows?
3. What are the most common content ratings on Netflix?

Libraries:
- pandas: for data loading, cleaning, and analysis
- matplotlib: for visualization
"""

import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_path):
    """Load the Netflix dataset from a CSV file."""
    try:
        df = pd.read_csv(file_path)
        print("✅ Dataset loaded successfully!")
        print("Rows:", len(df))
        print("Columns:", len(df.columns))
        return df
    except Exception as e:
        print("❌ Error loading data:", e)
        return None


def clean_data(df):
    """Clean the dataset by handling missing values."""
    print("🧹 Cleaning data...")
    df['country'].fillna('Unknown', inplace=True)
    df['rating'].fillna('Not Rated', inplace=True)
    df['duration'].fillna('Unknown', inplace=True)
    print("✅ Missing values handled.")
    return df


def question1(df):
    """Q1: Which countries produce the most Netflix titles?"""
    print("\n📊 Question 1: Top 10 countries with the most titles")
    country_counts = df['country'].value_counts().head(10)
    print(country_counts)

    country_counts.plot(kind='bar', color='skyblue', figsize=(8, 5))
    plt.title('Top 10 Countries with Most Netflix Titles')
    plt.xlabel('Country')
    plt.ylabel('Number of Titles')
    plt.tight_layout()
    plt.show()


def question2(df):
    """Q2: What is the average release year of Movies vs TV Shows?"""
    print("\n📊 Question 2: Average Release Year by Type")
    avg_years = df.groupby('type')['release_year'].mean().round(2)
    print(avg_years)

    avg_years.plot(kind='bar', color=['orange', 'lightgreen'], figsize=(6, 4))
    plt.title('Average Release Year: Movies vs TV Shows')
    plt.ylabel('Average Year')
    plt.tight_layout()
    plt.show()


def question3(df):
    """Q3: What are the most common content ratings on Netflix?"""
    print("\n📊 Question 3: Most Common Ratings")
    top_ratings = df['rating'].value_counts().head(10)
    print(top_ratings)

    top_ratings.plot(kind='bar', color='salmon', figsize=(7, 4))
    plt.title('Top 10 Most Common Netflix Ratings')
    plt.xlabel('Rating')
    plt.ylabel('Number of Titles')
    plt.tight_layout()
    plt.show()


def main():
    """Main function to execute the data analysis."""
    df = load_data('data/netflix_titles.csv')
    if df is not None:
        df = clean_data(df)
        question1(df)
        question2(df)
        question3(df)
    else:
        print("Exiting program due to data loading error.")


if __name__ == "__main__":
    main()
