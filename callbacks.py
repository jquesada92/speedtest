from dash.dependencies import Input, Output
import pandas as pd
from charts import line_chart_download_vs_upload, gauges_indicators
from charts.config import *
from os import environ

try: 
    speed_test_data = environ['SPEEDTEST_PARQUET']
except KeyError:
    seepd_test_data = 'data'


def register_Callback(app):
    @app.callback(
        Output("gauges_indicators", "figure"),
        Output("stream_line_chart", "figure"),
        [Input("interval-component", "n_intervals"),
        Input("moving_average","value")],
    )
    def streamFig(intervals,ma_value):
        print(ma_value)
        df = pd.read_parquet(seepd_test_data)
        df.index = df.timestamp
        if ma_value > 1 :
            df = df.rolling(ma_value)[["Upload_Mbps","Download_Mbps"]].mean()
        line_chart = line_chart_download_vs_upload(df)

        return gauges_indicators(df) , line_chart
