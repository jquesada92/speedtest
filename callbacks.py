from dash.dependencies import Input, Output
import pandas as pd
from charts import line_chart_download_vs_upload, gauges_indicators
from charts.config import *


def register_Callback(app):
    @app.callback(
        Output("gauges_indicators", "figure"),
        Output("stream_line_chart", "figure"),
        [Input("interval-component", "n_intervals")],
    )
    def streamFig(value):

        df = pd.read_parquet("measures")
        df.index = df.timestamp
        line_chart = line_chart_download_vs_upload(df)

        return gauges_indicators(df) , line_chart
