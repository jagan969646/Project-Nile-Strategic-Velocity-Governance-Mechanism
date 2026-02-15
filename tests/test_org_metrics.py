from src.metrics.org_metrics import calculate_span_of_control
import pandas as pd

def test_span():
    df = pd.DataFrame({
        "employee_id": [1,2],
        "manager_id": [None,1],
        "role_type": ["Manager","IC"]
    })
    result = calculate_span_of_control(df)
    assert result["span_of_control"].iloc[0] == 1