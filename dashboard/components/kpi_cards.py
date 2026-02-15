import streamlit as st

def kpi(title, value, delta=None, delta_color="normal", help_text=""):
    """
    Amazon-styled Metric Card with advanced delta support.
    
    Args:
        title (str): Metric label.
        value (str): Main display value.
        delta (str): Change indicator (e.g., "+5%").
        delta_color (str): "normal" (Green up/Red down), 
                          "inverse" (Red up/Green down), or "off".
        help_text (str): Tooltip explanation.
    """
    # Uses native st.metric which is styled by the global CSS in app.py
    st.metric(
        label=title, 
        value=value, 
        delta=delta, 
        delta_color=delta_color, 
        help=help_text
    )