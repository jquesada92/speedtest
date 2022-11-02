from dash.dependencies import Input, Output
import pandas as pd
from charts import multiplot_speedtest, Heatmaps
from charts.config import *
from os import environ

try: 
    DATA = environ['DATA']
except KeyError:
    DATA = 'calculations/data.parquet'


def register_Callback(app):
    @app.callback(
        Output("stream_line_chart", "figure"),
        [Input("interval-component", "n_intervals"),
        ],
    )
    def streamFig(intervals):

        df = pd.read_parquet(DATA)
        return multiplot_speedtest(df)


    @app.callback(
        Output("heatmaps", "figure"),
        [Input("interval-component", "n_intervals"),
        ],
    )
    def heatMaps(intervals):
        return Heatmaps()
 


    
