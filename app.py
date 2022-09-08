import pandas as pd
from dash import dcc, html, Dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output



from charts import line_chart_download_vs_upload, gauge_chart
from charts.config import *



app = Dash(__name__,)

# Create server variable with Flask server object for use with gunicorn
server = app.server


app.layout = html.Div([
    html.H1("Speed Test", style = {'color':'white'}),
            dcc.Interval(
            id='interval-component',
            interval=300000, # in milliseconds
            n_intervals=0
        ),
    
    
     dbc.Row([dbc.Col(dcc.Graph(id='gauge_download'), width=4, lg=3),
    dbc.Col(dcc.Graph(id='gauge_upload'), width=4, lg=3)]),
    dcc.Graph(id='stream_line_chart'),
],style={'background-color' :paper_bgcolor,"maxHeight": "400px"} )


# Define callback to update graph
@app.callback(
    
    Output('gauge_download', 'figure'),
    Output('gauge_upload', 'figure'),
    Output('stream_line_chart', 'figure'),
    [Input('interval-component', "n_intervals")]
)
def streamFig(value):
    
       
    df = pd.read_parquet('measures')
    df.index =df.timestamp
    gauge_chart_download = gauge_chart(df.iloc[-3:]['Download_Mbps'].mean(),steps=[[0,450],[450,600],[600,700]],title='Avg Download MBps', color = download_color)
    gauge_chart_upload = gauge_chart(df.iloc[-3:]['Upload_Mbps'].mean(),steps=[[0,10],[10,15],[15,20]],title='Avg Upload MBps', color = upload_color)
    line_chart =  line_chart_download_vs_upload(df)
    

    return gauge_chart_download, gauge_chart_upload, line_chart
    
app.run_server()

