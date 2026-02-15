import pandas as pd

def clean_financials():
    df = pd.read_csv("data/raw/aws_financials.csv")

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Fill missing values
    df["utilization_rate"] = df["utilization_rate"].fillna(df["utilization_rate"].mean())
    df["free_cash_flow"] = df["free_cash_flow"].fillna(0)

    # Ensure numeric
    df["capex"] = pd.to_numeric(df["capex"], errors="coerce")
    df["aws_revenue"] = pd.to_numeric(df["aws_revenue"], errors="coerce")

    # Save
    df.to_csv("data/processed/clean_financials.csv", index=False)

    return df


if __name__ == "__main__":
    clean_financials()