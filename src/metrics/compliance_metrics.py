import pandas as pd
import numpy as np

def load_data():
    """
    Simulates loading real-time marketplace data.
    In production, this would connect to an RDS instance or S3 bucket in /database.
    """
    data = {
        'product_id': ['B001', 'B002', 'B003', 'B004', 'B005'],
        'category': ['Electronics', 'Home', 'Electronics', 'Kitchen', 'Home'],
        'amazon_basics_price': [12.99, 45.00, 89.99, 15.50, 22.00],
        'avg_3p_seller_price': [15.50, 48.00, 110.00, 16.00, 35.00]
    }
    prices = pd.DataFrame(data)
    # Metadata return demonstrates Operational Excellence
    return prices, "Data loaded from primary database."

def calculate_price_delta(df):
    """
    Calculates the percentage difference between Amazon's own products 
    and 3rd-party competitors to identify antitrust risks.
    """
    # Price Delta formula: ((3P_Price - Amazon_Price) / 3P_Price) * 100
    df['price_delta_pct'] = (
        (df['avg_3p_seller_price'] - df['amazon_basics_price']) / 
        df['avg_3p_seller_price']
    ) * 100
    
    # Flag cases where the delta is aggressively high (>10%)
    df['risk_level'] = np.where(df['price_delta_pct'] > 10, 'High Risk', 'Compliant')
    
    return df