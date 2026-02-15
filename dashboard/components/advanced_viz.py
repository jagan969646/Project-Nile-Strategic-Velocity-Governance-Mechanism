import plotly.graph_objects as go
import plotly.express as px

def create_risk_gauge(value, title):
    """A high-end gauge for compliance risk."""
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = value,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': title, 'font': {'color': "#FF9900"}},
        gauge = {
            'axis': {'range': [None, 100], 'tickwidth': 1},
            'bar': {'color': "#FF9900"},
            'steps': [
                {'range': [0, 50], 'color': "#1a242f"},
                {'range': [50, 80], 'color': "#3e3e3e"},
                {'range': [80, 100], 'color': "#8b0000"}],
        }
    ))
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font={'color': "white", 'family': "Arial"}, height=250)
    return fig