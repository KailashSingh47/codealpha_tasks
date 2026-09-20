import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ----------------------------------------
# 1. Load Dataset
# ----------------------------------------

file_path = "Task_3_DataVisualization/dataset/superstore_sales.csv"

df = pd.read_csv(file_path)

# Convert Order_Date to datetime
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

print("Dataset loaded successfully!")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")
print()

# ----------------------------------------
# 2. Create Output Folder
# ----------------------------------------

output_folder = "Task_3_DataVisualization/visualizations"

os.makedirs(output_folder, exist_ok=True)

# ----------------------------------------
# 3. Sales by Category
# ----------------------------------------

category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(9, 6))

category_sales.plot(kind="bar")

plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    f"{output_folder}/sales_by_category.png",
    dpi=300
)

plt.close()

# ----------------------------------------
# 4. Sales by Region
# ----------------------------------------

region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(9, 6))

region_sales.plot(kind="bar")

plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    f"{output_folder}/sales_by_region.png",
    dpi=300
)

plt.close()

# ----------------------------------------
# 5. Profit by Category
# ----------------------------------------

category_profit = df.groupby("Category")["Profit"].sum().sort_values(
    ascending=False
)

plt.figure(figsize=(9, 6))

category_profit.plot(kind="bar")

plt.title("Total Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    f"{output_folder}/profit_by_category.png",
    dpi=300
)

plt.close()

# ----------------------------------------
# 6. Monthly Sales Trend
# ----------------------------------------

monthly_sales = (
    df.groupby(df["Order_Date"].dt.to_period("M"))["Sales"]
    .sum()
)

monthly_sales.index = monthly_sales.index.astype(str)

plt.figure(figsize=(12, 6))

plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    f"{output_folder}/monthly_sales_trend.png",
    dpi=300
)

plt.close()

# ----------------------------------------
# 7. Sales vs Profit
# ----------------------------------------

plt.figure(figsize=(9, 6))

sns.scatterplot(
    data=df,
    x="Sales",
    y="Profit",
    hue="Category"
)

plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")

plt.tight_layout()

plt.savefig(
    f"{output_folder}/sales_vs_profit.png",
    dpi=300
)

plt.close()

# ----------------------------------------
# 8. Top 10 Products by Sales
# ----------------------------------------

top_products = (
    df.groupby("Product")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))

top_products.sort_values().plot(kind="barh")

plt.title("Top 10 Products by Sales")
plt.xlabel("Sales")
plt.ylabel("Product")

plt.tight_layout()

plt.savefig(
    f"{output_folder}/top_10_products.png",
    dpi=300
)

plt.close()

# ----------------------------------------
# Finished
# ----------------------------------------

print("All visualizations created successfully!")

print("\nCreated files:")

for file in os.listdir(output_folder):
    print("-", file)