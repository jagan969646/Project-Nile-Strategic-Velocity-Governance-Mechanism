import streamlit as st
import sys, os
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# 1. INFRASTRUCTURE SETUP
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

try:
    from src.decision.decision_engine import hiring_decision, ai_spend_decision, compliance_decision
    from components.kpi_cards import kpi
except ImportError:
    st.error("Infrastructure Error: Check module paths.")

# 2. HEADER & MISSION
st.title("🕹️ S-Team Action Center")
st.markdown("### Decision Governance & FCF Impact Simulation")

# 3. SIDEBAR: THE MECHANISM TUNER
with st.sidebar:
    st.header("🛠️ Strategic Levers")
    st.info("Simulate 'Day 1' logic to optimize long-term Free Cash Flow.")
    
    span = st.slider("Target Span of Control", 1, 20, 10, help="Amazon Mandate: 10:1")
    roi = st.slider("Projected AI ROI Yield", -1.0, 3.0, 0.8)
    risk = st.slider("Regulatory Exposure Index", 0, 100, 25)
    
    st.divider()
    st.subheader("Principle Priority")
    # Highlighting cultural alignment
    st.success("✅ LP: Frugality (Active)")
    st.warning("⚠️ LP: Bias for Action (Critical Path)")

# 4. FINANCIAL SIMULATION (The 18LPA "Killer" Feature)
# Calculating theoretical FCF impact based on user inputs
base_fcf = 500.0  # Millions
savings_from_span = (span - 10) * 12.5  # Each point over 10 saves $12.5M
ai_revenue_boost = (roi * 45.0)        # Each ROI point adds $45M
risk_penalty = (risk * 2.5) if risk > 50 else 0

total_projected_fcf = base_fcf + savings_from_span + ai_revenue_boost - risk_penalty

# 5. MAIN LAYOUT
col_directives, col_visual = st.columns([1.5, 1], gap="large")

with col_directives:
    st.subheader("Executive Directives")
    
    # Logic-Driven Automated Memos
    if span < 10:
        st.error(f"🚨 **REORG REQUIRED:** {hiring_decision(span)}")
        st.caption(f"**Action:** Freeze all L6+ management hiring. Est. OpEx Waste: ${abs(savings_from_span):.1f}M.")
    else:
        st.success(f"✅ **TALENT OPTIMIZATION:** {hiring_decision(span)}")
        st.caption(f"**Action:** Approve aggressive L4/L5 backfills for high-span units.")

    st.warning(f"🧠 **AI CAPEX:** {ai_spend_decision(roi)}")
    st.info(f"⚖️ **RISK POSTURE:** {compliance_decision(risk)}")

    # NEW: Automated Directive Draft for CEO
    st.divider()
    st.subheader("📝 Draft CEO Directive")
    st.code(f"""
    TO: S-Team VPs
    FROM: S-Team Command (Simulation Engine)
    SUBJECT: Mandatory Efficiency Pivot
    
    Based on the current ROI yield of {roi}x, we are reallocating 
    capital to GPU clusters. Additionally, a span target of {span}:1 
    is now a binding constraint for Q4 planning.
    
    Est. FCF Impact: ${total_projected_fcf:.1f}M
    """, language="markdown")

with col_visual:
    st.subheader("Strategic Balance")
    
    # Financial Impact Gauge
    fig = go.Figure(go.Indicator(
        mode = "number+delta",
        value = total_projected_fcf,
        number = {'prefix': "$", 'suffix': "M"},
        delta = {'reference': 500, 'relative': False, 'position': "top"},
        title = {'text': "Projected Annual FCF Impact"},
        domain = {'x': [0, 1], 'y': [0, 1]}
    ))
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', font={'color': "white"}, height=250)
    st.plotly_chart(fig, use_container_width=True)

    # Risk Meter
    fig_risk = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = risk,
        gauge = {'axis': {'range': [0, 100]}, 'bar': {'color': "#FF9900"}},
        title = {'text': "Compliance Risk Level"},
    ))
    fig_risk.update_layout(paper_bgcolor='rgba(0,0,0,0)', font={'color': "white"}, height=200)
    st.plotly_chart(fig_risk, use_container_width=True)

# 6. KPI STRIP
st.divider()
k1, k2, k3 = st.columns(3)
with k1:
    kpi("OpEx Variance", f"${savings_from_span:+.1f}M", delta="Strategic Goal")
with k2:
    kpi("Decision Velocity", "+22%", delta="High Performance")
with k3:
    # Logic for Resource Elasticity
    status = "Optimal" if risk < 40 and span >= 10 else "Strained"
    kpi("Resource Elasticity", status, delta="S-Team Priority")