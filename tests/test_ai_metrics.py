import pandas as pd
from src.metrics.ai_metrics import calculate_revenue_yield

def test_revenue_yield():
    data = {
        "capex": [100, 200],
        "aws_revenue": [150, 300],
        "free_cash_flow": [50, 100]
    }

    df = pd.DataFrame(data)
    result = calculate_revenue_yield(df)

    assert "revenue_yield" in result.columns
    assert result["revenue_yield"].iloc[0] == 1.5