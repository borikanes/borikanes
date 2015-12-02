import sys
import os
import subprocess

# first_process = "screen -list | awk '{print $1}' | grep \"\.\.\"  | sed -n 1p"
# second_process = "screen -list | awk '{print $1}' | grep \"\.\.\"  | sed -n 2p"

first_process = os.popen('screen -list | awk \'{print $1}\' | grep \"\.\.\"  | sed -n 1p') # gets the first screen process
second_process = os.popen('screen -list | awk \'{print $1}\' | grep \"\.\.\"  | sed -n 2p') # gets second screen process
screen1 = str(first_process.read()).rstrip('\n')
screen2 = str(second_process.read()).rstrip('\n')

os.system("echo $(date +%A-%m-%d-%Y_%H-%M-%S) \"Else statement\" >> $BORIKANES_HOME/deploy_log")
os.system("cd $BORIKANES_HOME && git pull origin master")

screen1_quit = "screen -X -S "+first_process+" quit"
screen2_quit = "screen -X -S "+second_process+" quit"

if(first_process):
    os.system(screen1_quit)
    os.system("echo $(date +%A-%m-%d-%Y_%H-%M-%S) \"Killed first screen\" >> $BORIKANES_HOME/deploy_log")
if(second_process):
    os.system(screen2_quit)
    os.system("echo $(date +%A-%m-%d-%Y_%H-%M-%S) \"Killed second screen\" >> $BORIKANES_HOME/deploy_log")

os.system("cd $BORIKANES_HOME/node && screen -d -m npm start && cd $BORIKANES_HOME/flask && screen -d -m python3.4 flask_endpoints.py")
os.system("echo $(date +%A-%m-%d-%Y_%H-%M-%S) \"Deploy Succesfull!\" >> $BORIKANES_HOME/deploy_log")
