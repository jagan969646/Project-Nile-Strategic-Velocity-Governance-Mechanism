import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta
import os

fake = Faker()
np.random.seed(42)
random.seed(42)

# --------------------------------
# PATH SETUP (IMPORTANT)
# --------------------------------
# Get project root folder dynamically
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data", "raw")

# Create folder if it doesn't exist
os.makedirs(DATA_DIR, exist_ok=True)

# -------------------------------
# EMPLOYEE DATA
# -------------------------------

def generate_employees(n_employees=10000, n_departments=50):
    departments = [f"Dept_{i}" for i in range(1, n_departments + 1)]

    employees = []
    managers = []

    # Create Managers First
    for i in range(500):
        emp_id = i + 1
        managers.append(emp_id)
        employees.append({
            "employee_id": emp_id,
            "name": fake.name(),
            "department": random.choice(departments),
            "role_type": "Manager",
            "manager_id": None,
            "salary": random.randint(90000, 180000),
            "joining_date": fake.date_between(start_date="-8y", end_date="-2y"),
            "region": random.choice(["US", "EU", "India", "APAC"]),
            "performance_score": round(random.uniform(3, 5), 2)
        })

    # Create Individual Contributors
    for i in range(500, n_employees):
        emp_id = i + 1
        manager_id = random.choice(managers)

        employees.append({
            "employee_id": emp_id,
            "name": fake.name(),
            "department": random.choice(departments),
            "role_type": "IC",
            "manager_id": manager_id,
            "salary": random.randint(40000, 120000),
            "joining_date": fake.date_between(start_date="-5y", end_date="today"),
            "region": random.choice(["US", "EU", "India", "APAC"]),
            "performance_score": round(random.uniform(2, 5), 2)
        })

    return pd.DataFrame(employees)


# -------------------------------
# AI FINANCIAL DATA
# -------------------------------

def generate_financials(n_quarters=40):
    data = []
    base_capex = 20_000_000_000

    for q in range(n_quarters):
        capex = base_capex * (1 + 0.05 * q)
        revenue = capex * random.uniform(0.6, 1.1)
        utilization = random.uniform(40, 90)
        free_cash_flow = revenue - capex

        data.append({
            "quarter": f"Q{(q % 4) + 1} 20{20 + q//4}",
            "capex": int(capex),
            "aws_revenue": int(revenue),
            "utilization_rate": round(utilization, 2),
            "free_cash_flow": int(free_cash_flow)
        })

    return pd.DataFrame(data)


# -------------------------------
# MARKETPLACE PRICING DATA
# -------------------------------

def generate_marketplace(n_products=5000, n_prices=200000):
    products = []
    prices = []

    # Products
    for i in range(n_products):
        products.append({
            "product_id": i + 1,
            "category": random.choice(["Electronics", "Fashion", "Home", "Books"]),
            "brand": fake.company(),
            "is_amazon_owned": random.choice([True, False])
        })

    product_df = pd.DataFrame(products)

    # Prices
    for i in range(n_prices):
        prod_id = random.randint(1, n_products)
        amazon_price = round(random.uniform(10, 500), 2)
        seller_price = round(amazon_price * random.uniform(0.9, 1.2), 2)

        prices.append({
            "product_id": prod_id,
            "region": random.choice(["US", "EU", "India"]),
            "amazon_price": amazon_price,
            "seller_price": seller_price,
            "date": fake.date_between(start_date="-2y", end_date="today")
        })

    price_df = pd.DataFrame(prices)

    return product_df, price_df


# -------------------------------
# MAIN EXECUTION
# -------------------------------

if __name__ == "__main__":
    print("Generating Employees...")
    emp_df = generate_employees()
    emp_df.to_csv(os.path.join(DATA_DIR, "employees.csv"), index=False)

    print("Generating Financials...")
    fin_df = generate_financials()
    fin_df.to_csv(os.path.join(DATA_DIR, "aws_financials.csv"), index=False)

    print("Generating Marketplace...")
    prod_df, price_df = generate_marketplace()
    prod_df.to_csv(os.path.join(DATA_DIR, "products.csv"), index=False)
    price_df.to_csv(os.path.join(DATA_DIR, "prices.csv"), index=False)

    print("All Data Generated Successfully!")