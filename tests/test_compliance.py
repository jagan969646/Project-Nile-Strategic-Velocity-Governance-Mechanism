import pandas as pd
from src.metrics.compliance_metrics import calculate_price_delta

def test_price_delta():
    data = {
        "amazon_price": [100, 200],
        "seller_price": [120, 180]
    }

    df = pd.DataFrame(data)
    result = calculate_price_delta(df)

    assert "price_delta_pct" in result.columns
    assert result["price_delta_pct"].iloc[0] == 20.0