import dash_bootstrap_components as dbc
from dash import dcc, html
from charts.config import *


external_stylesheets = [dbc.themes.LUX]
config = {"displaylogo": False, "scrollZoom": False, "displayModeBar": False}

updates = dcc.Interval(
    id="interval-component", interval=300000, n_intervals=0  # in milliseconds
)
logo = dbc.Col(html.Img(src="https://www.pinclipart.com/picdir/big/491-4917274_panama-flag-png-palestine-flag-vector-clipart.png", height="30px"))



gauge_row = dbc.Row(
    [
        dbc.Col(

                    
                        dcc.Graph(id="gauge_download", config=config),
                    

            class_name="w-auto p-3",
        ),
        dbc.Col(
  
                        dcc.Graph(id="gauge_upload", config=config),
                    
             
            class_name="w-auto p-3",
        )
    ],
    style={"display": "flex", "background-color": paper_bgcolor},
)

streaming_row = dbc.Row(
    [ dbc.Col(
                dcc.Graph(id="stream_line_chart", config=config),
    width=12)],
    style={"display": "block", "background-color": paper_bgcolor},
)



layout =html.Div(
        [ updates, gauge_row, streaming_row],
        style={
            "background-color": paper_bgcolor,
            "width": "100%",
        },
    )