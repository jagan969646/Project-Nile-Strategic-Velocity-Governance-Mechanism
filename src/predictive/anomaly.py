import pandas as pd

def detect_anomalies(series, threshold=2):
    """
    Detect anomalies using Z-Score method.

    Parameters
    ----------
    series : pandas Series
        Numeric column (e.g., aws_revenue)
    threshold : int or float
        How many standard deviations away is considered anomaly

    Returns
    -------
    pandas DataFrame
        Rows where anomaly detected
    """

    mean = series.mean()
    std = series.std()

    # Z-score calculation
    z_scores = (series - mean) / std

    anomalies = series[abs(z_scores) > threshold]

    result = pd.DataFrame({
        "value": anomalies,
        "z_score": z_scores[anomalies.index]
    })

    return result
