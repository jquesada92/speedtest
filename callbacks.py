from dash.dependencies import Input, Output
import pandas as pd
from charts import multiplot_speedtest
from charts.config import *
from os import environ

try: 
    speed_test_data = environ['SPEEDTEST_PARQUET']
except KeyError:
    speed_test_data = 'data'


def register_Callback(app):
    @app.callback(
        Output("stream_line_chart", "figure"),
        [Input("interval-component", "n_intervals"),
        ],
    )
    def streamFig(intervals):

        df = pd.read_parquet(speed_test_data)
        df.index = df.timestamp
        return multiplot_speedtest(df)


    
