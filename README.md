# Crontab Assignment 

## Steps used in this assignment 
1. Create a VM instance with the basic settings on either GCP or Azure and launch 
2. Use the command ``` sudo apt-get update ``` to get the VM up to date
3. Check to see whether if <b> Crontab </b> is installed with
```sh 
crontab -h 
``` 
4. Select <b> nano </b> as the select-editor 
5. Make sure of the <b> python3 </b> and <b> python file </b> location with these commands
```sh 
which python 
```
```sh 
pwd
``` 
6. Open the <b> crontab </b> file with 
```sh 
crontab -e 
``` 
7. Type in the desired <b> crontab </b> schedule
8. Save it and exit the crontab file 
9. Check the status of cronjob with either command 
```sh 
systemctl status cron
```
<center> <b> or </center> </b>

```sh 
ls -l
```
#

## Crontab scheduled used: 

Once a Day: 
```sh 
0 2 * * * /usr/bin/python3 /home/wenjin/crontab/python.py
```
Sunday Night at 10:00 PM
```sh 
0 22 * * 0 /usr/bin/python3 /home/wenjin/crontab/python.py
```
At the end of every quarter 
```sh
0 0 1 */3 * /usr/bin/python3 /home/wenjin/crontab/python.py
```