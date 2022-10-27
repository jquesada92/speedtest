from dash import dcc, html
import dash_bootstrap_components as dbc
from charts.config import *


config = {"displaylogo": False, "scrollZoom": False, "displayModeBar": False}

updates = dcc.Interval(
    id="interval-component", interval=300000, n_intervals=0  # in milliseconds
)


navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="https://www.pinclipart.com/picdir/big/491-4917274_panama-flag-png-palestine-flag-vector-clipart.png", height="30px")),
                        dbc.Col(dbc.NavbarBrand("Network Speed Test by Jose Quesada", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="https://plotly.com",
                style={"textDecoration": "none"},
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            
        ]
    ),
    color=paper_bgcolor,
    dark=True,
)



resample_options = html.Div(
[
html.P('Resample optios:'),
dcc.RadioItems(   options=[
       {'label': 'Minutes', 'value': 'T'},
       {'label': 'Hours', 'value': 'H'},
       {'label': 'Days', 'value': 'D'},
   ],
        value='T',
        inline = False
    )],className='d-block')

rolling_options =  html.Div([
    html.P("Rolling:"),
    dcc.Slider(1, 24,1, value=1,  marks={
                            1: {'label': '1'},
                            12: {'label': '12'},
                            24: {'label': '24'}
                        },
                         updatemode='drag',
                          id = "moving_average")
])

#controls = dbc.Col([resample_options,html.Br(),rolling_options],width= 2, className='vw-25')

streaming_col = dbc.Col(dcc.Graph(id="stream_line_chart", config=config),className='d-inline vw-75')


layout = dbc.Container(
    
    [ navbar,dbc.Container([
    dcc.Store(id='last_32hrs'),

dbc.Row([updates ,
streaming_col],
            style={
                "background-color": paper_bgcolor,
                "color": default_fontcolor
            },
            
)])])