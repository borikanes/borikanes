import sys
import os
import subprocess

# os.system("echo $(date +%A-%m-%d-%Y_%H-%M-%S) \"About to kill screen sessions\" >> $BORIKANES_HOME/deploy_log")
error_variable = os.popen("screen -ls | grep Detached | cut -d. -f1 | awk \'{print $1}\' | xargs kill")
# os.system("echo $(date +%A-%m-%d-%Y_%H-%M-%S) \"Killed all screen sessions\" >> $BORIKANES_HOME/deploy_log")
os.system("cd $BORIKANES_HOME && git pull origin master")
os.system("cd $BORIKANES_HOME/node && sudo -u pi screen -d -m npm start && cd $BORIKANES_HOME/flask && sudo -u pi screen -d -m python3.4 flask_endpoints.py")
# os.system("echo "+restart_variable+" >> $BORIKANES_HOME/deploy_log")
# os.system("echo $(date +%A-%m-%d-%Y_%H-%M-%S) \"Deploy Succesfull!\" >> $BORIKANES_HOME/deploy_log")
