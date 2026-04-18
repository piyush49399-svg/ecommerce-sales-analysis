import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# LOAD DATASET
# ==============================
# Replace with your actual dataset file
df = pd.read_csv('ecommerce_product_dataset2.csv')

# ==============================
# 1. TOP 5 PRODUCTS BY REVENUE
# ==============================
top_products = (
    df.groupby("ProductName")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)
plt.figure(figsize=(8,5))
plt.grid(axis='y', linestyle='--', alpha=0.6)
top_products.plot(kind="bar")
plt.title("Top 5 Products by Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("results/top_products_revenue.png")

# ==============================
# 2. MONTHLY SALES TREND
# ==============================
df["DateAdded"] = pd.to_datetime(df["DateAdded"])

monthly_sales = (
    df.groupby(df["DateAdded"].dt.to_period("M"))["Sales"]
    .sum()
)

monthly_sales.index = monthly_sales.index.astype(str)

plt.figure(figsize=(8,5))
plt.grid(axis='y', linestyle='--', alpha=0.6)
monthly_sales.plot(marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid()
plt.tight_layout()
plt.savefig("results/monthly_sales_trend.png")


# ==============================
# 3. Top Cities by Sales Performance
# ==============================
top_customers = (
    df.groupby("City")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

plt.figure(figsize=(8,5))
plt.grid(axis='y', linestyle='--', alpha=0.6)
top_customers.plot(kind="bar")
plt.title("Top 5 Cities by Revenue")
plt.xlabel("City")
plt.ylabel("Revenue")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig("results/top_cities.png")
# ==============================
# SHOW ALL PLOTS
# ==============================
plt.show()