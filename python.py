import os 
import sys
import time
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

# create a new file in the current working directory
with open(cwd + '/home/foolishgod15/crontab/testfile_' + nowStr + '.txt', 'w') as f:
    f.write(str(covid_data))