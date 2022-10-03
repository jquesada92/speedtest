from datetime import datetime as dt,timedelta as td
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from .config import *





def line_chart_download_vs_upload(fig,df):
    
    now = dt.now()
    _24hrs_ago = now - td(hours=162)
    df = df.copy().loc[_24hrs_ago:now]
    x = df.index
    
    fig.add_trace(
        go.Scatter(
            x=x,
            y=df.Download_Mbps,
            name="Download (Mbps)",
            line=dict(color=download_color),

        ),row =2, col=1,
        secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(
            x=x, y=df.Upload_Mbps, name="Upload (Mbps)", line=dict(color=upload_color)
        ),row =2, col=1,
        secondary_y=True,
    )

    fig.update_layout(
        plot_bgcolor=plot_bgcolor,
        paper_bgcolor=paper_bgcolor,
        font=dict(color="white"),
        legend=dict(orientation="h", yanchor="bottom", y=-0.15, xanchor="right", x=1),
    )
    fig.update_xaxes(
        showgrid=False,
    )
    fig.update_yaxes(
        showgrid=False,
    )
    fig.update_yaxes(
        title_text="<b>Download (Mbps)</b> yaxis title",
        color=download_color,
        secondary_y=False,
    )
    fig.update_yaxes(
        title_text="<b>Upload (Mbps)</b> yaxis title",
        color=upload_color,
        secondary_y=True,
    )


def gauges_indicators(fig,df):

    def gauge_chart(value, steps, title, color):
        max_step = steps[-1][-1]
        title = f"{title} <span style='font-size:0.8em;color:gray'>MBps</span><br><span style='font-size:0.5em;color:gray'>Average</span>"
        gauge = go.Indicator(
                mode="gauge+number+delta",
                value=value,
                domain={"x": [0.1,1], "y":[0,0.85]},
                title={"text": title, "font": {"size": 32},'align': 'center' },
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

    last_test= df.iloc[-1]
    fig.add_trace(gauge_chart(
        last_test["Download_Mbps"],
        steps=[[0, 450], [450, 600], [600, 700]],
        title=f"<span style='font-size:0.8em;color:{download_color}'>Download</span>",
        color=download_color,
    )  ,row =1, col=1  )
    
    fig.add_trace( gauge_chart(
        last_test["Upload_Mbps"],
        steps=[[0, 10], [10, 15], [15, 20]],
        title=f"<span style='font-size:0.8em;color:{upload_color}'>Upload</span>",
        color=upload_color,
    ),row =1, col=2)
    fig.update_layout(
            paper_bgcolor=paper_bgcolor,
            font={"color": "white", "family": "Arial"},
        )
    fig.update_traces(number=dict(font=dict(size=36)),
        delta=dict(font=dict(size=30)), )
   
def multiplot_speedtest(df):
    fig = make_subplots(
    rows=2, cols=2,
    specs=[[{"type": "domain"}, {"type": "domain"}],
           [{"colspan": 2,"secondary_y":True}, None]],
           row_heights =[0.3,0.7])
    gauges_indicators(fig,df)
    line_chart_download_vs_upload(fig,df)
    fig.update_layout(height=600, margin=dict(l=0,r=0,b=0))
    
    return fig

    

