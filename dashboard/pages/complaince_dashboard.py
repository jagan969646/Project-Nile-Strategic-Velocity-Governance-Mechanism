import pandas as pd
import numpy as np
import sys
import os
import streamlit as st
import plotly.graph_objects as go

# 1. PATH SETUP
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from components.kpi_cards import kpi

# 2. DATA ENGINE
def load_data():
    """Simulates loading Amazon internal vs 3P pricing data."""
    data = {
        'product_id': ['B001', 'B002', 'B003', 'B004', 'B005', 'B006'],
        'category': ['Electronics', 'Home', 'Electronics', 'Kitchen', 'Home', 'Electronics'],
        'amazon_basics_price': [12.99, 45.00, 89.99, 15.50, 22.00, 105.00],
        'avg_3p_seller_price': [15.50, 48.00, 110.00, 16.00, 35.00, 108.00]
    }
    return pd.DataFrame(data)

def calculate_price_delta(df):
    """Calculates price gap and Parity Index."""
    df['price_delta_pct'] = ((df['avg_3p_seller_price'] - df['amazon_basics_price']) / df['avg_3p_seller_price']) * 100
    df['status'] = np.where(df['price_delta_pct'] > 15, '🚨 High Gap', '🟢 Parity')
    return df

# 3. OVERKILL VISUALIZATION
def plot_price_parity(df):
    """S-Team level price comparison chart."""
    fig = go.Figure()
    fig.add_trace(go.Bar(x=df['product_id'], y=df['avg_3p_seller_price'], name='3P Marketplace', marker_color='#808080'))
    fig.add_trace(go.Bar(x=df['product_id'], y=df['amazon_basics_price'], name='Amazon Basics', marker_color='#FF9900'))
    
    fig.update_layout(
        title="Internal vs. External Price Gap",
        barmode='group',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color="white"),
        height=350
    )
    return fig

# 4. DASHBOARD UI
st.title("⚖️ Antitrust Monitor: Price Parity Engine")

# Load and process
prices_df = load_data()
prices_df = calculate_price_delta(prices_df)

# OVERKILL KPI Logic
avg_delta = prices_df['price_delta_pct'].mean()
parity_index = 100 - avg_delta

col1, col2 = st.columns([1, 2])

with col1:
    st.metric("Global Parity Index", f"{parity_index:.1f}%", delta="-1.2%", delta_color="inverse")
    
    if parity_index < 90:
        st.error("🚨 CRITICAL: Parity Breach Detected")
        st.caption("Pricing gap in 'Electronics' exceeds safe-harbor 15% threshold.")
    else:
        st.success("✅ COMPLIANT: Pricing within limits")

with col2:
    st.plotly_chart(plot_price_parity(prices_df), use_container_width=True)

st.divider()

# Advanced product-level drilldown with gradient heatmap
st.subheader("Sub-Category Parity Audit")



st.dataframe(
    prices_df.style.background_gradient(subset=['price_delta_pct'], cmap='OrRd'),
    use_container_width=True,
    column_config={
        "amazon_basics_price": st.column_config.NumberColumn("AMZN ($)", format="$%.2f"),
        "avg_3p_seller_price": st.column_config.NumberColumn("3P Avg ($)", format="$%.2f"),
        "price_delta_pct": st.column_config.NumberColumn("Price Gap %", format="%.2f%%")
    }
)

# Crisis Feed placeholder
with st.expander("🕵️ Detailed Audit Log"):
    st.write(f"Audit completed at {pd.Timestamp.now()}")
    st.write("Source: Global Pricing Engine (LPA-18)")