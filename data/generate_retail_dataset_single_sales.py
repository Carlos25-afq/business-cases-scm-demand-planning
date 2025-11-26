import numpy as np
import pandas as pd
from datetime import datetime
import random

np.random.seed(42)
random.seed(42)

# PARAMETERS
N_STORES = 120
N_SKUS = 500
START_DATE = "2023-01-01"
END_DATE = "2024-06-30"
AVG_SKUS_PER_STORE_PER_DAY = 4  # Reduced slightly for file size
dates = pd.date_range(start=START_DATE, end=END_DATE, freq="D")

# ---------------------------------------------
# 1. STORES DATASET
# ---------------------------------------------
cities = [
    ("Paris", "France", 48.8566, 2.3522),
    ("Lyon", "France", 45.7640, 4.8357),
    ("Marseille", "France", 43.2965, 5.3698),
    ("Berlin", "Germany", 52.5200, 13.4050),
    ("Munich", "Germany", 48.1351, 11.5820),
    ("Madrid", "Spain", 40.4168, -3.7038),
    ("Barcelona", "Spain", 41.3851, 2.1734),
    ("Lisbon", "Portugal", 38.7223, -9.1393),
]

store_rows = []
stores_per_city = N_STORES // len(cities)

for i, (city, country, lat, lon) in enumerate(cities):
    for j in range(stores_per_city):
        store_id = f"ST{(i * stores_per_city) + j + 1:03d}"
        store_rows.append({
            "store_id": store_id,
            "store_name": f"{city} Store #{j+1}",
            "city": city,
            "country": country,
            "cluster": random.choice(["Urban", "Suburban", "Rural"]),
            "store_type": random.choice(["Supermarket", "Hypermarket", "Convenience"]),
            "latitude": lat + np.random.normal(0, 0.05),
            "longitude": lon + np.random.normal(0, 0.05)
        })

stores_df = pd.DataFrame(store_rows)
stores_df.to_csv("retail_stores_master.csv", index=False)

# ---------------------------------------------
# 2. PRODUCTS DATASET
# ---------------------------------------------
categories = [
    ("Beverages", ["Cola", "Juice", "Water"]),
    ("Snacks", ["Chips", "Chocolate", "Nuts"]),
    ("Dairy", ["Milk", "Yogurt", "Cheese"]),
    ("Personal Care", ["Soap", "Shampoo", "Deodorant"])
]

brands = ["BrandA", "BrandB", "BrandC", "BrandD"]
pack_sizes = ["250ml", "500ml", "1L", "200g", "500g", "1kg"]
units = ["unit", "pack", "bottle"]

sku_rows = []
for i in range(1, N_SKUS+1):
    cat, subcats = random.choice(categories)
    subcat = random.choice(subcats)
    brand = random.choice(brands)
    abc = np.random.choice(["A", "B", "C"], p=[0.2, 0.3, 0.5])
    sku_rows.append({
        "sku_id": f"SKU{i:04d}",
        "sku_name": f"{brand} {subcat}",
        "brand": brand,
        "category": cat,
        "subcategory": subcat,
        "pack_size": random.choice(pack_sizes),
        "unit": random.choice(units),
        "abc_class": abc,
        "base_price": round(np.random.uniform(1, 7), 2)
    })

sku_df = pd.DataFrame(sku_rows)
sku_df.to_csv("retail_products_master.csv", index=False)

# ---------------------------------------------
# 3. SUPPLIER LEADTIME
# ---------------------------------------------
suppliers = ["SUP1", "SUP2", "SUP3", "SUP4"]
supplier_rows = []

for sku in sku_df["sku_id"]:
    supplier_rows.append({
        "sku_id": sku,
        "supplier_id": random.choice(suppliers),
        "leadtime_mean": round(np.random.uniform(3, 15), 2),
        "leadtime_std": round(np.random.uniform(0.5, 4), 2)
    })

supplier_df = pd.DataFrame(supplier_rows)
supplier_df.to_csv("retail_supplier_leadtime.csv", index=False)

# ---------------------------------------------
# 4. SALES — SINGLE FILE
# ---------------------------------------------
sales_rows = []

print("Generating full sales dataset...")

for date in dates:
    for store in stores_df["store_id"]:
        skus_today = np.random.choice(sku_df["sku_id"], AVG_SKUS_PER_STORE_PER_DAY, replace=False)

        for sku in skus_today:
            base = np.random.uniform(5, 40)
            promo = np.random.choice([0, 1], p=[0.88, 0.12])
            multiplier = 1.4 if promo == 1 else 1.0
            demand = int(base * multiplier + np.random.normal(0, 2))

            sales_rows.append({
                "date": str(date.date()),
                "store_id": store,
                "sku_id": sku,
                "units_sold": max(0, demand),
                "promo_flag": promo
            })

sales_df = pd.DataFrame(sales_rows)

# Export as a single optimized CSV
sales_df.to_csv(
    "retail_sales_18months.csv",
    index=False,
    float_format="%.2f"
)

print("Sales file generated: retail_sales_18months.csv")

# ---------------------------------------------
# 5. STOCK LEVELS
# ---------------------------------------------
stock_rows = []

for idx, row in sales_df.iterrows():
    bo = np.random.uniform(20, 200)
    eo = max(0, bo - row["units_sold"] + np.random.uniform(-3, 5))
    stock_rows.append({
        "date": row["date"],
        "store_id": row["store_id"],
        "sku_id": row["sku_id"],
        "stock_begin_day": round(bo, 2),
        "stock_end_day": round(eo, 2)
    })

stock_df = pd.DataFrame(stock_rows)
stock_df.to_csv("retail_stock_levels_18months.csv", index=False)

# ---------------------------------------------
# 6. CALENDAR EVENTS
# ---------------------------------------------
calendar_df = pd.DataFrame({
    "date": dates,
    "is_month_start": dates.is_month_start.astype(int),
    "is_month_end": dates.is_month_end.astype(int),
    "is_weekend": dates.weekday >= 5
})

calendar_df.to_csv("retail_calendar_events.csv", index=False)

print("All datasets generated successfully.")
