import sys
import os
import subprocess

screen_process = os.popen('screen -list | awk \'{print $1}\' | grep "\.\."')
screen_process_clean = str(screen_process.read()).rstrip('\n')
if(not screen_process_clean):
    os.system("echo $(date +%A-%m-%d-%Y_%H-%M-%S) \"No screen sessions\" >> $BORIKANES_HOME/deploy_log && exit")
else:
    os.system("screen -ls | grep Detached | cut -d. -f1 | awk \'{print $1}\' | xargs kill")
    os.system("echo $(date +%A-%m-%d-%Y_%H-%M-%S) \"Killed all screen sessions\" >> $BORIKANES_HOME/deploy_log")
    os.system("cd $BORIKANES_HOME && git pull origin master && cd $BORIKANES_HOME/node && screen -d -m npm start && cd $BORIKANES_HOME/flask && screen -d -m python3.4 flask_endpoints.py")
    os.system("echo $(date +%A-%m-%d-%Y_%H-%M-%S) \"Deploy Succesfull!\" >> $BORIKANES_HOME/deploy_log")
