from os import environ
try:
    log_folder = environ['SPEEDTEST_LOG']
except KeyError:
    log_folder = "log"

try: 
    speed_test_data = environ['SPEEDTEST_PARQUET']
except KeyError:
    speed_test_data = 'data'

#