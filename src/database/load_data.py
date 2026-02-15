import pandas as pd
import sqlite3
import os

# ensure database folder exists
os.makedirs("database", exist_ok=True)

conn = sqlite3.connect("database/amazon.db")

emp = pd.read_csv("data/processed/clean_employees.csv")
fin = pd.read_csv("data/processed/clean_financials.csv")
price = pd.read_csv("data/processed/clean_prices.csv")

emp.to_sql("employees", conn, if_exists="replace", index=False)
fin.to_sql("financials", conn, if_exists="replace", index=False)
price.to_sql("prices", conn, if_exists="replace", index=False)

conn.close()
print("Database Loaded Successfully")