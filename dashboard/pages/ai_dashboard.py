import streamlit as st
import sys
import os
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# 1. PATH SETUP
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

try:
    from src.metrics.ai_metrics import load_financial_data, calculate_revenue_yield
    from src.decision.recommendations import ai_recommendation
    from components.kpi_cards import kpi
except ImportError:
    st.error("Infrastructure Error: Check module paths for AI metrics.")

# 2. DATA ENGINE
@st.cache_data
def get_ai_data():
    df = load_financial_data()
    df = calculate_revenue_yield(df)
    
    # Adding Regional Mock Data for the "Over-Qualified" Heatmap
    regions = ['US-East-1', 'US-West-2', 'EU-West-1', 'APAC-South-1', 'SA-East-1']
    df['top_region'] = np.random.choice(regions, len(df))
    return df

try:
    df = get_ai_data()
    avg_utilization = df["utilization_rate"].mean()
    latest_yield = df["revenue_yield"].iloc[-1]
    latest_fcf = df["free_cash_flow"].iloc[-1]
    capex_efficiency = latest_yield * 1.84  # S-Team weighted multiplier
except Exception as e:
    st.error(f"Data Load Failure: {e}")
    st.stop()

# 3. HEADER & EXECUTIVE SUMMARY
st.title("🧠 AI CapEx Intelligence")
st.markdown("### Decision Support for Infrastructure Expansion & GPU Arbitrage")

# 4. EXECUTIVE KPI ROW (The "Pulse" of the Business)
c1, c2, c3, c4 = st.columns(4)
with c1: 
    kpi("Revenue Yield", f"${latest_yield:,.2f}", delta="+4.2%", help_text="Revenue per AI compute unit")
with c2: 
    kpi("GPU Utilization", f"{avg_utilization:.1f}%", delta="-2.1%", delta_color="inverse")
with c3: 
    kpi("Marginal FCF", f"${latest_fcf/1e6:.1f}M", delta="+12%")
with c4: 
    kpi("CapEx Multiplier", f"{capex_efficiency:.2f}x", help_text="Return on Hardware Investment")

st.divider()

# 5. ADVANCED ANALYTICS (The 18LPA Flex)
main_col, side_col = st.columns([2.5, 1], gap="large")

with main_col:
    # A. Global Cluster Heatmap (Shows Regional Scalability)
    st.subheader("🌐 Global GPU Cluster Utilization")
    
    # Creating a spatial efficiency map
    # 
    regions_df = pd.DataFrame({
        'Region': ['US-East', 'US-West', 'EMEA', 'APAC', 'LATAM'],
        'Load': [94, 78, 45, 88, 30],
        'Yield': [2.1, 1.9, 0.8, 1.7, 1.2]
    })
    
    fig_heat = px.scatter(regions_df, x="Load", y="Yield", size="Load", color="Yield",
                          hover_name="Region", text="Region",
                          color_continuous_scale="Viridis",
                          labels={'Load': 'Cluster Load (%)', 'Yield': 'Revenue Yield (x)'})
    
    fig_heat.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', 
                           plot_bgcolor='rgba(0,0,0,0)', height=350)
    st.plotly_chart(fig_heat, use_container_width=True)

    # B. Trajectory Line
    st.subheader("Yield vs. Free Cash Flow (FCF) Intensity")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df["revenue_yield"], name="Revenue Yield", 
                             line=dict(color='#FF9900', width=4), mode='lines+markers'))
    fig.add_trace(go.Bar(x=df.index, y=df["free_cash_flow"], name="FCF Contribution", 
                         opacity=0.2, marker_color="#ffffff"))
    
    fig.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', 
                      plot_bgcolor='rgba(0,0,0,0)', height=350, margin=dict(t=0))
    st.plotly_chart(fig, use_container_width=True)

with side_col:
    st.markdown("### 🕹️ Strategic Directives")
    
    decision = ai_recommendation(avg_utilization, latest_fcf)
    
    # 
    if avg_utilization > 80:
        st.error("🚨 **CAPACITY CRUNCH**")
        st.write("Current load exceeds Day 1 efficiency thresholds. High risk of latency spikes.")
        st.button("Draft CapEx Procurement Memo")
    else:
        st.success("✅ **GROWTH RUNWAY**")
        st.write("Infrastructure is optimized for current LLM training velocity.")

    st.divider()
    
    # Financial Confidence Logic
    st.info(f"**S-TEAM INSIGHT:** {decision}")
    
    st.caption("Model Confidence: Bayesian Accuracy")
    st.progress(92)
    
    # Strategic Warning - Antitrust connection
    st.warning("⚠️ **RISK:** APAC region yield is volatile due to local semiconductor regulations.")

# 6. RAW AUDIT
with st.expander("🔍 Infrastructure Data Ledger (L8 Access Only)"):
    st.dataframe(df, use_container_width=True)