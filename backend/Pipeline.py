from glob import glob
import re
from datetime import datetime as dt
from os import remove, environ
import pandas as pd
from time import sleep

class SpeedTestLogs:

    def __init__(self,path):
        self.path = path
        
        
    def retrive_information(self,file):
        try:
    
            filter_empty_lines = lambda x: list(filter(lambda __x: __x != '',x)) 
            split_lines = lambda x: filter_empty_lines(x.split('\n'))
            retrieve_float = lambda pattern, string:  float(re.search(pattern,string).group(1))

            def open_log(file):
                with open(file,'r') as f:
                    text = f.read()
                return text
            sleep(10)
            text = open_log(file)
            date =  re.search("(\d{14})\n\n",text).group(1)
            data = {'timestamp' : [dt.strptime(date,"%Y%m%d%H%M%S").strftime("%Y-%m-%d %H:%M:%S")],
                'Download_Mbps' : [retrieve_float("Download:\s+(\d+\.{0,1}\d+)\s+Mbps\s+",text)],
                'Upload_Mbps' : [retrieve_float("Upload:\s+(\d+\.{0,1}\d+)\s+Mbps\s+",text)]}
            pd.DataFrame.from_dict(data=data).assign(timestamp = lambda x : pd.to_datetime(x.timestamp)).to_parquet(f"""{environ['path_parquet_speedtest']}/{date}.parquet""")
            remove(file)
        except Exception as er: 
            print(file,er)
    
    def convert_test_into_log(self):
        
        
        list(map(self.retrive_information, glob(f"{self.path}/*.txt")))
        
            
    


speed_test_pipeline = SpeedTestLogs(path=environ['path_data_speedtest'])
speed_test_pipeline.convert_test_into_log()

