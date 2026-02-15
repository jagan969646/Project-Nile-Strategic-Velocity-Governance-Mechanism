import sys
import os

# --- Fix Python Path ---
CURRENT_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, "..", ".."))
sys.path.append(PROJECT_ROOT)

import pandas as pd
from utils.logger import get_logger

logger = get_logger("employee_cleaner")

RAW_PATH = os.path.join(PROJECT_ROOT, "data", "raw", "employees.csv")
PROCESSED_PATH = os.path.join(PROJECT_ROOT, "data", "processed", "clean_employees.csv")


def clean_employees():
    logger.info("Starting employee data cleaning...")

    # Check file exists
    if not os.path.exists(RAW_PATH):
        logger.error("employees.csv not found in data/raw/")
        return

    df = pd.read_csv(RAW_PATH)

    # -------------------------
    # BASIC CLEANING
    # -------------------------
    df.drop_duplicates(inplace=True)

    if "name" in df.columns:
        df["name"] = df["name"].fillna("Unknown")

    if "joining_date" in df.columns:
        df["joining_date"] = pd.to_datetime(df["joining_date"], errors="coerce")

    if "salary" in df.columns:
        df = df[df["salary"] > 0]

    if "performance_score" in df.columns:
        df["performance_score"] = df["performance_score"].clip(1, 5)

    # -------------------------
    # DERIVED FIELDS
    # -------------------------
    if "joining_date" in df.columns:
        df["tenure_years"] = (
            (pd.Timestamp.today() - df["joining_date"]).dt.days / 365
        ).round(2)

    if "role_type" in df.columns:
        df["is_manager"] = df["role_type"].apply(
            lambda x: 1 if str(x).lower() == "manager" else 0
        )

    # -------------------------
    # SAVE OUTPUT
    # -------------------------
    os.makedirs(os.path.dirname(PROCESSED_PATH), exist_ok=True)
    df.to_csv(PROCESSED_PATH, index=False)

    logger.info(f"Employee cleaning complete. Rows saved: {len(df)}")


if __name__ == "__main__":
    clean_employees()
