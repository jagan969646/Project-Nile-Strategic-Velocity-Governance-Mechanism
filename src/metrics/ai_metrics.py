import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data", "raw")

def load_financial_data():
    path = os.path.join(DATA_DIR, "aws_financials.csv")
    return pd.read_csv(path)


def calculate_revenue_yield(df):
    df["revenue_yield"] = df["aws_revenue"] / df["capex"]
    return df


def utilization_efficiency(df):
    df["utilization_efficiency"] = df["utilization_rate"] / 100
    return df


def roi_signal_score(df):
    # Weighted score
    df["roi_score"] = (
        (df["revenue_yield"] * 0.5) +
        (df["utilization_efficiency"] * 0.3) +
        ((df["free_cash_flow"] > 0).astype(int) * 0.2)
    )
    return df


def free_cash_flow_trend(df):
    df["fcf_trend"] = df["free_cash_flow"].diff()
    return df


if __name__ == "__main__":
    df = load_financial_data()

    df = calculate_revenue_yield(df)
    df = utilization_efficiency(df)
    df = roi_signal_score(df)
    df = free_cash_flow_trend(df)

    print(df.head())