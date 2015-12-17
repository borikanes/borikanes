import sys
import os
import subprocess

os.system("cd $BORIKANES_HOME && git pull origin master")
os.system("echo $(date +%A-%m-%d-%Y_%H-%M-%S) \"Killed all screen sessions\" >> $BORIKANES_HOME/deploy_log")
os.system("echo \"SHould have worked\" >> $BORIKANES_HOME/deploy_log")
os.system("echo \"SHould have worked1\" >> $BORIKANES_HOME/deploy_log")
os.system("echo \"SHould have worked2\" >> $BORIKANES_HOME/deploy_log")
os.system("echo \"SHould have worked3\" >> $BORIKANES_HOME/deploy_log")
os.system("echo $(date +%A-%m-%d-%Y_%H-%M-%S) \"Deploy Succesfull!\" >> $BORIKANES_HOME/deploy_log")
error_variable = os.popen("screen -ls | grep Detached | cut -d. -f1 | awk \'{print $1}\' | xargs kill")
# os.system("echo $(date +%A-%m-%d-%Y_%H-%M-%S) \"Killed all screen sessions\" >> $BORIKANES_HOME/deploy_log")
# os.system("cd $BORIKANES_HOME && git pull origin master")
os.system("cd $BORIKANES_HOME/node && screen -d -m npm start && cd $BORIKANES_HOME/flask && screen -d -m python3.4 flask_endpoints.py")
# os.system("echo "+restart_variable+" >> $BORIKANES_HOME/deploy_log")
# os.system("echo $(date +%A-%m-%d-%Y_%H-%M-%S) \"Deploy Succesfull!\" >> $BORIKANES_HOME/deploy_log")
