import pandas as pd
from config import speed_test_data
from time import sleep
from datetime import datetime as dt,timedelta as td

def read_data():
    return pd.read_parquet(f"../{speed_test_data}")

def get_corr(df,by='day_of_week'):

    
    DOWNLOAD_MBPS = 600
    UPLOAD_MBPS = 15
    norm_speed = lambda s,speed_limit: 1 - ((speed_limit - s)/speed_limit)

    if  by == "day_of_week":
        col = by
        index = 'weeknum'
        var = ['Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday',  'Saturday','Sunday']
    elif by == 'part_of_the_date':
        col = by
        index = 'date'
        var = ['Morning','Afternoon','Evening','Night']
        
    agg_df = df[[index,col, 'Download_Mbps', 'Upload_Mbps']].copy()\
                            .assign(Download_Mbps = lambda x: norm_speed(x.Download_Mbps,DOWNLOAD_MBPS),
                                   Upload_Mbps = lambda x: norm_speed(x.Upload_Mbps,UPLOAD_MBPS))\
                            .groupby([index,col],as_index=False).mean()\
                             .set_index(index)
    melt_df = pd.melt(agg_df.reset_index(), id_vars=[index,by], value_vars=['Download_Mbps', 'Upload_Mbps'])
    melt_df.pivot_table(index=['variable'],columns=col,values='value',aggfunc='mean')[var].to_parquet(f'../calculations/{by}.parquet')


        



while True:
    df = read_data()
    get_corr(df,by='day_of_week')
    get_corr(df,by='part_of_the_date')
    last_30_days = dt.now().date() - td(days=30)
    df.set_index('timestamp').loc[last_30_days: ].copy().sort_index().to_parquet('../calculations/data.parquet')
    sleep(60*15)