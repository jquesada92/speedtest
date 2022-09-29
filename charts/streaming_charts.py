from datetime import datetime as dt,timedelta as td
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from .config import *




def line_chart_download_vs_upload(df):
    
    now = dt.now()
    _24hrs_ago = now - td(hours=162)
    df = df.copy().loc[_24hrs_ago:now]
    x = df.index
    line_chart = make_subplots(specs=[[{"secondary_y": True}]])



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
        title="Speed Download Vs Upload (Mbps)",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
         margin=dict(l=5, r=5),
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

def gauges_indicators(df):

    def gauge_chart(value,x,y, steps, title, color):
        max_step = steps[-1][-1]
        title = f"{title} <span style='font-size:0.8em;color:gray'>MBps</span><br><span style='font-size:0.5em;color:gray'>Average</span>"
        gauge = go.Indicator(
                mode="gauge+number+delta",
                value=value,
                domain={"x": x, "y": y},
                title={"text": title, "font": {"size": 18},'align': 'center' },
                delta={"reference": steps[-1][0], "increasing": {"color": color}},
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
        
       
        return gauge

    sample = df.iloc[-3:]
    
    fig = go.Figure()
    fig.add_trace(gauge_chart(
        sample["Download_Mbps"].mean(),
        [0.1,1],
        [0.55,0.85],
        steps=[[0, 450], [450, 600], [600, 700]],
        title=f"<span style='font-size:0.8em;color:{download_color}'>Download</span>",
        color=download_color,
    )    )
    
    fig.add_trace( gauge_chart(
        sample["Upload_Mbps"].mean(),
        [0.1,1],
        [0,0.35],
        steps=[[0, 10], [10, 15], [15, 20]],
        title=f"<span style='font-size:0.8em;color:{upload_color}'>Upload</span>",
        color=upload_color,
    ))
    fig.update_layout(
            paper_bgcolor=paper_bgcolor,
            font={"color": "white", "family": "Arial"},
            margin=dict(l=5, r=5,b=5,t=5),
        )
    fig.update_traces(number=dict(font=dict(size=32)),
        delta=dict(font=dict(size=25)), )
    return fig
    
