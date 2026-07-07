import plotly.express as px


def plot_basic_columns(df, x_col, y_col):
    fig = px.scatter(
        df,
        x=x_col,
        y=y_col,
        title=f"{y_col} vs {x_col}",
        trendline="ols"
    )

    fig.update_layout(
        height=500,
        template="plotly_white"
    )

    return fig
