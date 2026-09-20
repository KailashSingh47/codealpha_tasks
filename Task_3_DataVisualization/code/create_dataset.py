import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

categories = {
    "Furniture": ["Chair", "Table", "Bookcase", "Filing Cabinet"],
    "Office Supplies": ["Paper", "Binder", "Pen", "Storage Box"],
    "Technology": ["Laptop", "Monitor", "Keyboard", "Mouse", "Printer"]
}

regions = ["East", "West", "Central", "South"]
segments = ["Consumer", "Corporate", "Home Office"]

rows = []

start_date = datetime(2023, 1, 1)

for order_id in range(1, 1001):
    order_date = start_date + timedelta(days=random.randint(0, 729))

    category = random.choice(list(categories.keys()))
    product = random.choice(categories[category])
    region = random.choice(regions)
    segment = random.choice(segments)

    sales = round(random.uniform(20, 1500), 2)
    profit = round(sales * random.uniform(-0.10, 0.30), 2)
    quantity = random.randint(1, 10)

    rows.append([
        order_id,
        order_date.strftime("%Y-%m-%d"),
        region,
        segment,
        category,
        product,
        quantity,
        sales,
        profit
    ])

columns = [
    "Order_ID",
    "Order_Date",
    "Region",
    "Segment",
    "Category",
    "Product",
    "Quantity",
    "Sales",
    "Profit"
]

df = pd.DataFrame(rows, columns=columns)

output_path = "Task_3_DataVisualization/dataset/superstore_sales.csv"

df.to_csv(output_path, index=False)

print("Dataset created successfully!")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")
print(f"Saved to: {output_path}")