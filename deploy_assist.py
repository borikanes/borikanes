import sys
import os
import subprocess

os.system("echo $(date +%A-%m-%d-%Y_%H-%M-%S) \"Running script......\" >> $BORIKANES_HOME/deploy_log")
os.system("cd $BORIKANES_HOME && git pull origin master")
#os.system("screen -ls | grep Detached | cut -d. -f1 | awk \'{print $1}\' | xargs kill")
os.system("echo $(date +%A-%m-%d-%Y_%H-%M-%S) \"Killed all screen sessions\" >> $BORIKANES_HOME/deploy_log")
os.system("cd $BORIKANES_HOME/node && screen -d -m npm start && cd $BORIKANES_HOME/flask && screen -d -m python3.4 flask_endpoints.py")
os.system("echo $(date +%A-%m-%d-%Y_%H-%M-%S) \"Deploy Succesfull!\" >> $BORIKANES_HOME/deploy_log")
