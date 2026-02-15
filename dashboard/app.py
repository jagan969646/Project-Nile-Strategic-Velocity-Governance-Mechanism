import streamlit as st
import os
import time

# 1. PAGE CONFIG (Executive Grade)
st.set_page_config(
    page_title="AMZN S-TEAM | COMMAND CENTER",
    page_icon="Logo.jpg",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. STRATEGIC NAVIGATION (The "Single Source of Truth")
pages_dict = {
    "Strategic Crisis": [
        st.Page("pages/org_dashboard.py", title="Bureaucracy Tax Audit", icon="📉"),
        st.Page("pages/ai_dashboard.py", title="AI CapEx Efficiency", icon="🧠"),
    ],
    "Regulatory Compliance": [
        st.Page("pages/complaince_dashboard.py", title="Antitrust Monitor", icon="⚖️"),
    ],
    "Decision Intelligence": [
        st.Page("pages/predictive_dashboard.py", title="Predictive Forecasting", icon="📡"),
        st.Page("pages/decision_dashboard.py", title="Action Center", icon="🕹️"),
    ]
}

# 3. ADVANCED S-TEAM UI (Glassmorphism & Neural Glow)
st.markdown("""
<style>
    .stApp { background: radial-gradient(circle at 20% 10%, #0f172a 0%, #020617 100%); }
    
    /* Top Header - S-Team Persistent Overlay */
    .s-team-header {
        background: rgba(255, 255, 255, 0.02);
        border-bottom: 2px solid rgba(255, 153, 0, 0.3);
        padding: 20px 40px;
        margin: -80px -100px 40px -100px;
        backdrop-filter: blur(20px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }

    /* Professional Metric Cards */
    div[data-testid="stMetric"] {
        background: rgba(30, 41, 59, 0.4) !important;
        border: 1px solid rgba(255, 255, 255, 0.05) !important;
        border-radius: 16px !important;
        padding: 15px !important;
    }
    
    /* Neon Status Pulses */
    .pulse-amber { height: 10px; width: 10px; background-color: #FF9900; border-radius: 50%; display: inline-block; animation: pulse-orange 2s infinite; margin-right: 10px; }
    .pulse-red { height: 10px; width: 10px; background-color: #ff4b4b; border-radius: 50%; display: inline-block; animation: pulse-red 1s infinite; margin-right: 10px; }
    
    @keyframes pulse-orange { 0% { box-shadow: 0 0 0 0 rgba(255, 153, 0, 0.7); } 70% { box-shadow: 0 0 0 10px rgba(255, 153, 0, 0); } 100% { box-shadow: 0 0 0 0 rgba(255, 153, 0, 0); } }
    @keyframes pulse-red { 0% { box-shadow: 0 0 0 0 rgba(255, 75, 75, 0.7); } 70% { box-shadow: 0 0 0 10px rgba(255, 75, 75, 0); } 100% { box-shadow: 0 0 0 0 rgba(255, 75, 75, 0); } }
</style>
""", unsafe_allow_html=True)

# 4. SIDEBAR (The Executive Override)
with st.sidebar:
    if os.path.exists("Logo.jpg"):
        st.image("Logo.jpg", width=160)
    
    st.markdown("<h2 style='text-align: center; color: #FF9900; letter-spacing: 3px; font-weight: 300;'>S-TEAM COMMAND</h2>", unsafe_allow_html=True)
    st.divider()
    
    # Persistent State Controller
    st.subheader("🛠️ Global Variables")
    status = st.select_slider("System Priority", options=["Day 1", "Stable", "Warning", "Crisis"], value="Stable")
    region = st.selectbox("Market Context", ["Global Operations", "North America", "EMEA", "APAC"])
    
    st.divider()
    
    # CEO Meta-Search
    st.markdown("### 🔍 Strategic Metric Search")
    all_pages = {p.title: p for cat in pages_dict.values() for p in cat}
    search_query = st.selectbox("Jump to Analysis...", options=["Select Metric"] + list(all_pages.keys()), label_visibility="collapsed")
    
    st.divider()
    st.caption(f"Kernel Version: 4.2.0-AMZN | Latency: 2ms")

# 5. GLOBAL HEADER (Live Risk/Efficiency Engine)
with st.container():
    st.markdown('<div class="s-team-header">', unsafe_allow_html=True)
    col_logo, col_stat1, col_stat2, col_stat3 = st.columns([0.6, 0.8, 1, 2.5])
    
    with col_logo:
        if os.path.exists("Logo.jpg"):
            st.image("Logo.jpg", width=85)
            
    with col_stat1:
        st.caption("CAPEX YIELD")
        st.subheader("1.84x")
        
    with col_stat2:
        st.caption("OPERATIONAL STATE")
        mode_color = "#FF9900" if status == "Day 1" else ("#ff4b4b" if status == "Crisis" else "#ffffff")
        st.markdown(f"<h3 style='margin:0; color:{mode_color}; letter-spacing:1px;'>{status.upper()}</h3>", unsafe_allow_html=True)
        
    with col_stat3:
        st.caption("STRATEGIC RISK & FCF PROJECTION")
        # Over-qualified feature: A reactive status bar
        risk_val = 85 if status == "Crisis" else (10 if status == "Day 1" else 35)
        st.progress(risk_val / 100)
        
        if status == "Crisis":
            st.markdown('<p style="font-size:0.85rem;"><span class="pulse-red"></span><b style="color:#ff4b4b;">CRITICAL:</b> Anti-trust exposure in EMEA. Est. FCF impact: -$1.2B.</p>', unsafe_allow_html=True)
        elif status == "Day 1":
            st.markdown('<p style="font-size:0.85rem;"><span class="pulse-amber"></span><b>OPPORTUNITY:</b> AI efficiency surplus. Potential to accelerate Q4 roadmap by 3 weeks.</p>', unsafe_allow_html=True)
        else:
            st.markdown('<p style="font-size:0.85rem;">Systems nominal. Bureaucracy Tax holding steady at 4.2%.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# 6. RUN NAVIGATION
pg = st.navigation(pages_dict)
pg.run()