from functools import reduce

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from .config import *


def line_chart_download_vs_upload(df):

    # Create figure with secondary y-axis
    line_chart = make_subplots(specs=[[{"secondary_y": True}]])

    # Add traces

    x = df.index

    line_chart.add_trace(
        go.Scatter(
            x=x,
            y=df.Download_Mbps,
            name="Download (Mbps)",
            line=dict(color=download_color),
        ),
        secondary_y=False,
    )

    line_chart.add_trace(
        go.Scatter(
            x=x, y=df.Upload_Mbps, name="Upload (Mbps)", line=dict(color=upload_color)
        ),
        secondary_y=True,
    )

    line_chart.update_layout(
        plot_bgcolor=plot_bgcolor,
        paper_bgcolor=paper_bgcolor,
        font=dict(color="white"),
        title="Download Vs Upload (Mbps)",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )
    line_chart.update_xaxes(
        showgrid=False,
    )
    line_chart.update_yaxes(
        showgrid=False,
    )
    line_chart.update_yaxes(
        title_text="<b>Download (Mbps)</b> yaxis title",
        color=download_color,
        secondary_y=False,
    )
    line_chart.update_yaxes(
        title_text="<b>Upload (Mbps)</b> yaxis title",
        color=upload_color,
        secondary_y=True,
    )

    return line_chart


def gauge_chart(value, steps, title, color):

    max_step = steps[-1][-1]

    gauge = go.Figure(
        go.Indicator(
            mode="gauge+number+delta",
            value=value,
            domain={"x": [0, 1], "y": [0, 1]},
            title={"text": title, "font": {"size": 24}},
            delta={"reference": steps[-1][0], "increasing": {"color": "RebeccaPurple"}},
            gauge={
                "axis": {
                    "range": [None, max_step],
                    "tickwidth": 2,
                    "tickcolor": plot_bgcolor,
                },
                "bar": {"color": color},
                "bgcolor": "white",
                "borderwidth": 2,
                "bordercolor": "gray",
                "steps": [
                    {"range": steps[0], "color": "#ff6188"},
                    {"range": steps[1], "color": "#fc9867"},
                    {"range": steps[2], "color": "#a9dc76"},
                ],
            },
        )
    )
    gauge.update_layout(
        paper_bgcolor=paper_bgcolor,
        font={"color": "white", "family": "Arial"},
    )
    return gauge
