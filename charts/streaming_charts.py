import plotly.graph_objects as go
from plotly.subplots import make_subplots
from .config import *
from pandas import read_parquet




def line_chart_download_vs_upload(fig,df):
    
    df = df.copy()
    x = df.index
    
    fig.add_trace(
    go.Scatter(
        x=x, y=df.ping, name="Ping", line=dict(color='white')
    ),row =1, col=2,
    )
    fig.update_yaxes(
    title_text="<b>Ping</b>",
    color='white',
    rangemode = 'tozero',
    showgrid=False,
    row =1, col=2,
    )



    
    fig.add_trace(
        go.Scatter(
            x=x, y=df.Upload_Mbps, name="Upload (Mbps)", line=dict(color=upload_color)
        ),row =2, col=2,
    )
    fig.update_yaxes(
    title_text="<b>Upload (Mbps)</b>",
    color=upload_color,
    rangemode = 'tozero',
     showgrid=False,
    row =2, col=2,
    )



    fig.add_trace(
        go.Scatter(
            x=x,
            y=df.Download_Mbps,
            name="Download (Mbps)",
            line=dict(color=download_color),

        ),row =3, col=2,
    )

    fig.update_yaxes(
        title_text="<b>Download (Mbps)</b>",
        color=download_color,
        rangemode = 'tozero',
         showgrid=False,
        row =3, col=2,
    )

    fig.update_xaxes(
        showgrid=False,
    )

    fig.update_layout(
        plot_bgcolor=plot_bgcolor,
        paper_bgcolor=paper_bgcolor,
        font=dict(color="white"),
        legend=dict(orientation="h", yanchor="bottom", y=-0.15, xanchor="right", x=1),
    )
   
   


def gauges_indicators(fig,value):

    def gauge_chart(value, steps, title, color):
        max_step = steps[-1][-1]
        title = f"{title} <span style='font-size:0.8em;color:gray'>MBps</span><br><span style='font-size:0.5em;color:gray'>Average</span>"
        gauge = go.Indicator(
                mode="gauge+number+delta",
                value=value,
                domain={"x": [0.25,0.55], "y":[0.25,0.55]},
                title={"text": title, "font": {"size": 25},'align': 'center' },
                delta={"reference": steps[-1][0],  "font": {"size": 13},"increasing": {"color": color}},
                number={"font": {"size": 25}},
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

    

    
    fig.add_trace( gauge_chart(
        value["Upload_Mbps"],
        steps=[[0, 10], [10, 15], [15, 20]],
        title=f"<span style='font-size:0.8em;color:{upload_color}'>Upload</span>",
        color=upload_color,
    ),row =2, col=1)

    fig.add_trace(gauge_chart(
        value["Download_Mbps"],
        steps=[[0, 450], [450, 600], [600, 700]],
        title=f"<span style='font-size:0.8em;color:{download_color}'>Download</span>",
        color=download_color,
    )  ,row =3, col=1 )

    fig.update_layout(
            paper_bgcolor=paper_bgcolor,
            font={"color": "white", "family": "Arial"},
            showlegend=False
        )
    fig.update_traces(
        number=dict(font=dict(size=28)),
        delta=dict(font=dict(size=25))
        )

def ping_number(fig,value):

    title = "Ping"
    fig.add_trace(

            go.Indicator(
                mode = "number",
                value = value,
                domain = {'x': [0, 1], 'y': [0, 1]},
                title={"text": title, "font": {"size": 25},'align': 'center' },
                number={"font": {"size": 25}}),
                row =1, col=1

    )

   
def multiplot_speedtest(df):

    fig = make_subplots(
    rows=3, cols=2,
    specs=[
            [{"type": "domain"}, {} ],
            [ {"type": "domain"}, {}],
            [{"type": "domain"},{}]
    ],
    column_widths = [0.30,0.70],
    row_heights = [0.22,0.38,0.38],
    horizontal_spacing=0.1, 
    vertical_spacing=0.25,
          )
    
    values = df.mean()
    gauges_indicators(fig,values)
    ping_number(fig,values['ping'])
    line_chart_download_vs_upload(fig,df)
    fig.update_layout(height=545, margin=dict(l=30,r=30,b=30,t=35))
    
    return fig

    

def Heatmaps():
    
    heatmap = lambda df: go.Heatmap(x=df.columns,z=df.values,y=list(map(lambda x:x.replace('_','<br>'),df.index)), colorscale='Spectral',zmax=1,zmin=0)
    fig = make_subplots(1, 2,column_widths = [0.30,0.70],)
    fig.add_trace(heatmap(read_parquet('calculations/part_of_the_date.parquet')),row=1, col=1)
    fig.add_trace(heatmap(read_parquet('calculations/day_of_week.parquet')),row=1, col=2)
    fig.update_layout(
            paper_bgcolor=paper_bgcolor,
            font={"color": "white", "family": "Arial"},
            height=300, margin=dict(l=0,r=0,b=20,t=10)
        )
    return fig