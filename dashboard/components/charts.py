import plotly.graph_objects as go

def plot_price_parity(df):
    """High-end comparison chart for S-Team review."""
    fig = go.Figure()
    
    # 3P Seller Prices (The Baseline)
    fig.add_trace(go.Scatter(
        x=df['product_id'], y=df['avg_3p_seller_price'],
        mode='lines+markers', name='3P Marketplace Avg',
        line=dict(color='#808080', dash='dash')
    ))
    
    # Amazon Basics Prices (The Competitor)
    fig.add_trace(go.Scatter(
        x=df['product_id'], y=df['amazon_basics_price'],
        mode='lines+markers', name='Amazon Basics',
        line=dict(color='#FF9900', width=4)
    ))

    fig.update_layout(
        title="Internal vs. External Price Parity",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color="white"),
        yaxis_title="Price ($)"
    )
    return fig