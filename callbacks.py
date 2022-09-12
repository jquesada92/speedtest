
from dash.dependencies import Input, Output
import pandas as pd
from charts import line_chart_download_vs_upload, gauge_chart
from charts.config import *

def register_Callback(app):

    @app.callback(
    Output("gauge_download", "figure"),
    Output("gauge_upload", "figure"),
    Output("stream_line_chart", "figure"),
    [Input("interval-component", "n_intervals")],)
    def streamFig(value):

        df = pd.read_parquet("measures")
        df.index = df.timestamp
        gauge_chart_download = gauge_chart(
            df.iloc[-3:]["Download_Mbps"].mean(),
            steps=[[0, 450], [450, 600], [600, 700]],
            title="Avg Download MBps",
            color=download_color,
        )
        gauge_chart_upload = gauge_chart(
            df.iloc[-3:]["Upload_Mbps"].mean(),
            steps=[[0, 10], [10, 15], [15, 20]],
            title="Avg Upload MBps",
            color=upload_color,
        )
        line_chart = line_chart_download_vs_upload(df)

        return gauge_chart_download, gauge_chart_upload, line_chart








