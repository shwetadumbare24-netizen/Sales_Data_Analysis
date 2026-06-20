import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("sales_data.csv")

print("\nOriginal Data:\n")
print(df)

# Check missing values
print("\nMissing Values:\n")
print(df.isnull().sum())

# Filter sales greater than 3000
high_sales = df[df["Sales"] > 3000]

print("\nProducts with Sales > 3000:\n")
print(high_sales)

# Group by category
category_sales = df.groupby("Category")["Sales"].sum()

print("\nTotal Sales by Category:\n")
print(category_sales)

# Plot graph
category_sales.plot(kind="bar")
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()