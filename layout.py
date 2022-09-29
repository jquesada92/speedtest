from dash import dcc, html
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
    class_name="d-inline g-0",
    width=2,
)

streaming_col = dbc.Col([dbc.Row(dcc.Graph(id="stream_line_chart", config=config),class_name="d-block"),
 dbc.Row(dcc.Slider(1, 24,1, value=1, id = "moving_average"),class_name="d-block w-95 mx-15")
], class_name='d-inline ml-5')


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
    fluid = True

)
