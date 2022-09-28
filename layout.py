from dash import dcc
import dash_bootstrap_components as dbc
from charts.config import *


config = {"displaylogo": False, "scrollZoom": False, "displayModeBar": False}

updates = dcc.Interval(
    id="interval-component", interval=300000, n_intervals=0  # in milliseconds
)

gauge_col = dbc.Col(
    [
    dcc.Graph(id="gauges_indicators", config=config)
    ],
    style={"background-color": paper_bgcolor},
    class_name="g-0",
    width=2,
)

streaming_col = dbc.Col(dcc.Graph(id="stream_line_chart", config=config), class_name='ml-5')

layout = dbc.Container(
    [
        dbc.Row(
            [updates, gauge_col, streaming_col],
            style={
                "background-color": paper_bgcolor,
            },
            class_name="g-0",
        )
    ],
)
