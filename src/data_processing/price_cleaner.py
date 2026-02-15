import pandas as pd

def clean_prices():
    df = pd.read_csv("data/raw/prices.csv")

    df.drop_duplicates(inplace=True)

    # Remove invalid prices
    df = df[(df["amazon_price"] > 0) & (df["seller_price"] > 0)]

    # Add delta
    df["price_delta"] = df["amazon_price"] - df["seller_price"]

    # Save
    df.to_csv("data/processed/clean_prices.csv", index=False)

    return df


if __name__ == "__main__":
    clean_prices()