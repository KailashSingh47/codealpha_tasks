import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from scipy.stats import pearsonr

# ---------------------------------------
# LOAD DATA
# ---------------------------------------

df = pd.read_csv("books_dataset.csv")

os.makedirs("screenshots", exist_ok=True)

# ---------------------------------------
# BASIC DATA EXPLORATION
# ---------------------------------------

print("=" * 60)
print("EXPLORATORY DATA ANALYSIS - BOOKS DATASET")
print("=" * 60)

print("\n1. DATASET SHAPE")
print(df.shape)

print("\n2. COLUMNS")
print(df.columns.tolist())

print("\n3. DATA TYPES")
print(df.dtypes)

print("\n4. MISSING VALUES")
print(df.isnull().sum())

print("\n5. DUPLICATE ROWS")
print(df.duplicated().sum())

# ---------------------------------------
# STATISTICAL SUMMARY
# ---------------------------------------

print("\n6. STATISTICAL SUMMARY")
print(df[["Price", "Rating"]].describe())

# ---------------------------------------
# PRICE ANALYSIS
# ---------------------------------------

print("\n7. PRICE ANALYSIS")

mean_price = df["Price"].mean()
median_price = df["Price"].median()
minimum_price = df["Price"].min()
maximum_price = df["Price"].max()

print("Minimum Price:", minimum_price)
print("Maximum Price:", maximum_price)
print("Mean Price:", mean_price)
print("Median Price:", median_price)

# ---------------------------------------
# RATING ANALYSIS
# ---------------------------------------

print("\n8. RATING DISTRIBUTION")
print(df["Rating"].value_counts().sort_index())

# ---------------------------------------
# AVAILABILITY
# ---------------------------------------

print("\n9. AVAILABILITY")
print(df["Availability"].value_counts())

# ---------------------------------------
# OUTLIER DETECTION USING IQR
# ---------------------------------------

Q1 = df["Price"].quantile(0.25)
Q3 = df["Price"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[
    (df["Price"] < lower_bound) |
    (df["Price"] > upper_bound)
]

print("\n10. PRICE OUTLIER ANALYSIS")
print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)
print("Number of Price Outliers:", len(outliers))

if len(outliers) > 0:
    print("\nOutlier Books:")
    print(outliers[["Title", "Price", "Rating"]])
else:
    print("No price outliers detected using the IQR method.")

# ---------------------------------------
# HYPOTHESIS TEST
# ---------------------------------------

print("\n11. HYPOTHESIS TEST")

print("Question:")
print("Is there a relationship between book price and rating?")

print("\nNull Hypothesis (H0):")
print("There is no linear relationship between price and rating.")

print("\nAlternative Hypothesis (H1):")
print("There is a linear relationship between price and rating.")

correlation, p_value = pearsonr(
    df["Price"],
    df["Rating"]
)

print("\nPearson Correlation:", correlation)
print("P-value:", p_value)

if p_value < 0.05:
    print("Result: Statistically significant relationship detected.")
else:
    print("Result: No statistically significant linear relationship detected at the 5% significance level.")

# ---------------------------------------
# TOP AND BOTTOM PRICED BOOKS
# ---------------------------------------

print("\n12. MOST EXPENSIVE BOOKS")
print(
    df[["Title", "Price", "Rating"]]
    .sort_values("Price", ascending=False)
    .head(10)
)

print("\n13. CHEAPEST BOOKS")
print(
    df[["Title", "Price", "Rating"]]
    .sort_values("Price")
    .head(10)
)

# ---------------------------------------
# VISUALIZATIONS
# ---------------------------------------

sns.set_theme(style="whitegrid")

# 1. Price Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df["Price"], bins=15, kde=True)
plt.title("Distribution of Book Prices")
plt.xlabel("Price")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("screenshots/price_distribution.png")
plt.close()

# 2. Rating Distribution
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x="Rating")
plt.title("Distribution of Book Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("screenshots/rating_distribution.png")
plt.close()

# 3. Price by Rating
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x="Rating", y="Price")
plt.title("Book Price by Rating")
plt.xlabel("Rating")
plt.ylabel("Price")
plt.tight_layout()
plt.savefig("screenshots/price_by_rating.png")
plt.close()

# 4. Availability
plt.figure(figsize=(10, 6))
sns.countplot(
    data=df,
    x="Availability",
    order=df["Availability"].value_counts().index
)
plt.title("Book Availability")
plt.xlabel("Availability")
plt.ylabel("Number of Books")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("screenshots/availability.png")
plt.close()

# 5. Correlation Heatmap
numeric_df = df.select_dtypes(include=np.number)

plt.figure(figsize=(8, 6))
sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Correlation Between Numerical Variables")
plt.tight_layout()
plt.savefig("screenshots/correlation_heatmap.png")
plt.close()

# 6. Price Outlier Boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(y=df["Price"])
plt.title("Price Outlier Detection")
plt.ylabel("Price")
plt.tight_layout()
plt.savefig("screenshots/price_outliers.png")
plt.close()

# ---------------------------------------
# SAVE EDA REPORT
# ---------------------------------------

with open("eda_report.txt", "w", encoding="utf-8") as report:

    report.write("CODEALPHA TASK 2 - EXPLORATORY DATA ANALYSIS\n")
    report.write("=" * 55 + "\n\n")

    report.write("DATASET OVERVIEW\n")
    report.write("-" * 30 + "\n")
    report.write(f"Rows: {df.shape[0]}\n")
    report.write(f"Columns: {df.shape[1]}\n")
    report.write(f"Missing values: {df.isnull().sum().sum()}\n")
    report.write(f"Duplicate rows: {df.duplicated().sum()}\n\n")

    report.write("PRICE ANALYSIS\n")
    report.write("-" * 30 + "\n")
    report.write(f"Minimum price: {minimum_price:.2f}\n")
    report.write(f"Maximum price: {maximum_price:.2f}\n")
    report.write(f"Mean price: {mean_price:.2f}\n")
    report.write(f"Median price: {median_price:.2f}\n\n")

    report.write("RATING DISTRIBUTION\n")
    report.write("-" * 30 + "\n")
    report.write(df["Rating"].value_counts().sort_index().to_string())
    report.write("\n\n")

    report.write("OUTLIER ANALYSIS\n")
    report.write("-" * 30 + "\n")
    report.write(f"Number of price outliers: {len(outliers)}\n")
    report.write(f"Lower IQR bound: {lower_bound:.2f}\n")
    report.write(f"Upper IQR bound: {upper_bound:.2f}\n\n")

    report.write("HYPOTHESIS TEST\n")
    report.write("-" * 30 + "\n")
    report.write("H0: No linear relationship between price and rating.\n")
    report.write("H1: A linear relationship exists between price and rating.\n")
    report.write(f"Pearson correlation: {correlation:.4f}\n")
    report.write(f"P-value: {p_value:.4f}\n")

    if p_value < 0.05:
        report.write("Conclusion: A statistically significant linear relationship was detected at the 5% significance level.\n")
    else:
        report.write("Conclusion: No statistically significant linear relationship was detected at the 5% significance level.\n")

print("\n" + "=" * 60)
print("EDA COMPLETED SUCCESSFULLY")
print("=" * 60)
print("Charts saved in: screenshots/")
print("Report saved as: eda_report.txt")
