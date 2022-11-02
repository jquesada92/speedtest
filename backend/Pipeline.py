from glob import glob
import re
from datetime import datetime as dt
from os import remove
import pandas as pd
from config import speed_test_data, log_folder



class SpeedTestLogs:
    
    def __init__(self,path):
        self.path = path
        
        
    def retrive_information(self,file):
        try:
    
            retrieve_float = lambda pattern, string:  float(re.search(pattern,string).group(1))

            def open_log(file):
                with open(file,'r') as f:
                    text = f.read()
                return text
            text = open_log(file)
            date =  re.search("(\d{14})\n\n",text).group(1)
            data = {'timestamp' : [dt.strptime(date,"%Y%m%d%H%M%S").strftime("%Y-%m-%d %H:%M:%S")],
                'Download_Mbps' : [retrieve_float("Download:\s+(\d+\.{0,1}\d+)\s+Mbps\s+",text)],
                'Upload_Mbps' : [retrieve_float("Upload:\s+(\d+\.{0,1}\d+)\s+Mbps\s+",text)],
                'ping':[retrieve_float("Idle Latency:\s+(\d+\.{0,1}\d+)\s+ms",text)]}
            df = pd.DataFrame.from_dict(data=data).assign(timestamp = lambda x : pd.to_datetime(x.timestamp))
            df['day_of_week'] = df.timestamp.dt.day_name()
            df['weeknum'] = df.timestamp.dt.isocalendar().week
            df['date'] = df.timestamp.dt.date
            df['part_of_the_date'] = df.timestamp.dt.hour.apply(lambda x : 'Morning' if (x>=5)&(x<12) else 'Afternoon' if (x>=12)&(x<17) else 'Evening' if (x>=17)&(x<21) else 'Night' )
            df.to_parquet(f"""{speed_test_data}/{date}.parquet""")
            remove(file)
        except Exception as er: 
            print(file,er)
            remove(file)
        
            
    
    def convert_test_into_log(self):
        list(map(self.retrive_information, glob(f"{self.path}/*.txt")))

    
        

speed_test_pipeline = SpeedTestLogs(path=log_folder)

while True:
    speed_test_pipeline.convert_test_into_log()







