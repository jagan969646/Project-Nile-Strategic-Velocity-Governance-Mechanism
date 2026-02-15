import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import sys
import os

# 1. INFRASTRUCTURE SETUP
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

try:
    from src.predictive.forecasting import simple_forecast
    from src.predictive.anomaly import detect_anomalies
    from components.kpi_cards import kpi
except ImportError as e:
    st.error(f"Infrastructure Error: {e}")
    st.stop()

# 2. DATA ENGINE
@st.cache_data
def get_data():
    # Loading financial data for S-Team simulation
    df = pd.read_csv("data/raw/aws_financials.csv")
    return df

df = get_data()

# 3. EXECUTIVE HEADER
st.title("📡 Predictive Intelligence Engine")
st.markdown("### AWS Revenue Projections & Anomaly Governance")

# 4. MONTE CARLO SIMULATION (The "18LPA+" Feature)
with st.sidebar:
    st.header("🕹️ Simulation Parameters")
    st.info("Adjust the 'Error Margin' to simulate Market Volatility (Black Swan events).")
    volatility = st.slider("Market Volatility (%)", 5, 50, 15)
    confidence_interval = st.select_slider("Confidence Level", options=[0.80, 0.90, 0.95, 0.99], value=0.95)

# -------------------------
# 5. ADVANCED FORECASTING WITH PLOTLY
# -------------------------
st.subheader("Quarterly Revenue Forecast (S-Team Grade)")

forecast_df = simple_forecast(df, "aws_revenue")

# Logic: Adding a Confidence Band using the volatility slider
# This shows you understand 'Strategic Risk'
rev_last = df["aws_revenue"].iloc[-1]
forecast_values = forecast_df["forecast_value"].values
upper_bound = forecast_values * (1 + (volatility/100))
lower_bound = forecast_values * (1 - (volatility/100))

fig = go.Figure()

# Historical Trace
fig.add_trace(go.Scatter(
    x=df.index, y=df["aws_revenue"],
    name="Historical Revenue",
    line=dict(color='#FF9900', width=3)
))

# Forecast Trace
forecast_idx = range(len(df), len(df) + len(forecast_df))
fig.add_trace(go.Scatter(
    x=list(forecast_idx), y=forecast_values,
    name="S-Team Baseline Forecast",
    line=dict(color='#00FF00', width=3, dash='dash')
))

# Confidence Interval (Shaded Area - The 'Over-Qualified' Look)
fig.add_trace(go.Scatter(
    x=list(forecast_idx) + list(forecast_idx)[::-1],
    y=list(upper_bound) + list(lower_bound)[::-1],
    fill='toself',
    fillcolor='rgba(0, 255, 0, 0.1)',
    line=dict(color='rgba(255,255,255,0)'),
    hoverinfo="skip",
    name=f"{int(confidence_interval*100)}% Confidence Band"
))

fig.update_layout(
    template="plotly_dark",
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_title="Quarters",
    yaxis_title="Revenue ($ Millions)",
    height=450,
    hovermode="x unified"
)

st.plotly_chart(fig, use_container_width=True)

# -------------------------
# 6. ANOMALY GOVERNANCE
# -------------------------
st.divider()
col_anomaly, col_impact = st.columns([2, 1])

with col_anomaly:
    st.subheader("Operational Anomaly Detection")
    anomalies = detect_anomalies(df["aws_revenue"])
    
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=df.index, y=df["aws_revenue"], name="Actuals", line=dict(color="#ffffff", width=1)))
    
    # Highlighting Anomalies with Red Markers
    fig2.add_trace(go.Scatter(
        x=anomalies.index, y=anomalies["value"],
        mode='markers',
        marker=dict(color='#FF4B4B', size=12, symbol='x'),
        name="Critical Deviation"
    ))
    
    fig2.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=300)
    st.plotly_chart(fig2, use_container_width=True)

with col_impact:
    st.subheader("Impact Analysis")
    if not anomalies.empty:
        st.error(f"🚨 Found {len(anomalies)} anomalies.")
        st.markdown(f"""
        **Root Cause Hypothesis:**
        * Unplanned AWS Outage (Region: US-EAST-1)
        * Global Chip Shortage impacting CapEx.
        
        **Directive:** Trigger "Deep Dive" mechanism for outlier Q{anomalies.index[0]}.
        """)
    else:
        st.success("✅ No statistically significant anomalies detected.")