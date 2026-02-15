import pandas as pd

def simple_forecast(df, column, periods=4):
    """
    Simple growth-rate based forecast.

    Parameters
    ----------
    df : pandas DataFrame
        Data containing the column to forecast
    column : str
        Column name (e.g., "aws_revenue")
    periods : int
        Number of future periods to predict

    Returns
    -------
    pandas DataFrame
        Forecasted values
    """

    data = df.copy()

    # Calculate growth rate
    data["growth_rate"] = data[column].pct_change()

    avg_growth = data["growth_rate"].mean()

    last_value = data[column].iloc[-1]

    forecasts = []
    for i in range(periods):
        next_value = last_value * (1 + avg_growth)
        forecasts.append(round(next_value, 2))
        last_value = next_value

    forecast_df = pd.DataFrame({
        "period": [f"Future_Q{i+1}" for i in range(periods)],
        "forecast_value": forecasts
    })

    return forecast_df