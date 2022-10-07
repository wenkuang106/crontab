import os 
import sys
import time
import crontab
import pandas as pd

# get current working directory
cwd = os.getcwd()
# print cwd
print(cwd)

# get the current time
now = time.time()
# save current time as a string
nowStr = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(now))

## reading the JSON API data from healthdata.gov
covid_data = pd.read_json('https://healthdata.gov/resource/6xf2-c3ie.json')
