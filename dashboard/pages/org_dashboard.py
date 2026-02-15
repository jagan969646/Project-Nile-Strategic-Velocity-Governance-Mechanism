import streamlit as st
import sys
import os
import pandas as pd
import plotly.express as px

# 1. PATH SETUP
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

try:
    from src.metrics.org_metrics import load_employee_data, calculate_span_of_control
    from components.kpi_cards import kpi
    from components.recommendation_engine import get_strategic_advice 
except ImportError as e:
    st.error(f"Infrastructure Error: {e}")
    st.stop()

# 2. DATA ENGINE
try:
    df = load_employee_data()
    span_df = calculate_span_of_control(df)
    
    total_ee = len(df)
    manager_count = df[df["role_type"] == "Manager"].shape[0]
    avg_span = span_df["span_of_control"].mean()
    
    target_span = 10
    required_managers = total_ee / target_span
    excess_managers = max(0, manager_count - required_managers)
    bureaucracy_tax = (excess_managers / total_ee) * 100 

except Exception as e:
    st.error(f"Critical Data Load Failure: {e}")
    st.stop()

# 3. HEADER & KPI ROW
st.title("📉 Organization Efficiency Audit")
st.markdown("### Bureaucracy Tax & Span of Control Monitor")

c1, c2, c3, c4 = st.columns(4)
with c1: kpi("Total Headcount", f"{total_ee:,}")
with c2: kpi("Current Managers", f"{manager_count:,}")
with c3: kpi("Avg Span", f"{avg_span:.1f}:1", delta=f"{avg_span-10:.1f}", delta_color="inverse")
with c4: kpi("Target Ratio", "10:1")

st.divider()

# 4. MAIN LAYOUT
col_main, col_side = st.columns([3, 1], gap="large")

with col_main:
    st.subheader("Departmental Span Distribution")
    
    # FIX: Using span_df.index explicitly to avoid 'department' ValueError
    fig = px.bar(
        span_df, 
        x=span_df.index, 
        y="span_of_control",
        color="span_of_control",
        color_continuous_scale=["#FF4B4B", "#FF9900", "#00FF00"],
        labels={'index': 'Business Unit', 'span_of_control': 'Span Ratio'},
        template="plotly_dark"
    )
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=380)
    st.plotly_chart(fig, use_container_width=True)

    # 5. STRATEGIC ROADMAP (With Safety Check)
    st.subheader("🚀 Strategic Improvement Roadmap")
    advice_list = get_strategic_advice(avg_span, bureaucracy_tax, 1.5)
    
    # FIX: Check if list is empty to avoid st.columns(0) error
    if advice_list:
        rec_cols = st.columns(len(advice_list))
        for i, advice in enumerate(advice_list):
            with rec_cols[i]:
                st.markdown(f"""
                <div style="background: rgba(255, 153, 0, 0.05); border: 1px solid rgba(255, 153, 0, 0.3); padding: 15px; border-radius: 10px; height: 180px;">
                    <p style="color: #FF9900; font-size: 0.7rem; font-weight: bold; margin: 0;">LP: {advice['principle'].upper()}</p>
                    <p style="font-size: 0.9rem; font-weight: bold; margin: 5px 0;">{advice['action']}</p>
                    <p style="font-size: 0.75rem; color: #BDC3C7; line-height: 1.2;">{advice['rationale']}</p>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.success("✅ No critical improvements required. Organization is operating at peak 'Day 1' efficiency.")

with col_side:
    st.markdown("### 💡 Executive Insights")
    tax_color = "#FF4B4B" if bureaucracy_tax > 5 else "#FF9900"
    st.markdown(f"""
        <div style="background: rgba(255, 75, 75, 0.1); border: 1px solid {tax_color}; padding: 20px; border-radius: 15px; text-align: center;">
            <p style="margin:0; font-size: 0.8rem; opacity: 0.8;">BUREAUCRACY TAX</p>
            <h1 style="margin:0; color: {tax_color};">{bureaucracy_tax:.1f}%</h1>
        </div>
    """, unsafe_allow_html=True)
    
    if avg_span < 10:
        st.error("🚨 **MANDATE BREACH**")
        st.write("Current Span is below 10:1. Decision speed is at risk.")
    else:
        st.success("✅ **HEALTHY STRUCTURE**")