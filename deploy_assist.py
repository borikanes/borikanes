import sys
import os
import subprocess

screen_process = os.popen('screen -list | awk \'{print $1}\' | grep "\.\."')
screen_process_clean = str(screen_process.read()).rstrip('\n')
if(not screen_process_clean):
    os.system("echo $(date +%A-%m-%d-%Y_%H-%M-%S) \"No screen sessions\" >> $BORIKANES_HOME/deploy_log && exit")
else:
    first_process = os.popen('screen -list | awk \'{print $1}\' | grep \"\.\.\"  | sed -n 1p') # gets the first screen process
    second_process = os.popen('screen -list | awk \'{print $1}\' | grep \"\.\.\"  | sed -n 2p') # gets second screen process
    screen1 = str(first_process.read()).rstrip('\n')
    screen2 = str(second_process.read()).rstrip('\n')

    os.system("echo $(date +%A-%m-%d-%Y_%H-%M-%S) \"Else statement\" >> $BORIKANES_HOME/deploy_log")
    os.system("cd $BORIKANES_HOME && git pull origin master")

    screen1_quit = "screen -X -S "+screen1+" quit"
    screen2_quit = "screen -X -S "+screen2+" quit"

    print_first = "echo "+ screen1+ " >> $BORIKANES_HOME/deploy_log"
    print_second = "echo "+ screen2+ " >> $BORIKANES_HOME/deploy_log"
    os.system(print_first)
    os.system(print_second)

    if(second_process):
        os.system(screen2_quit)
        os.system("echo $(date +%A-%m-%d-%Y_%H-%M-%S) \"Killed second screen\" >> $BORIKANES_HOME/deploy_log")

    if(first_process):
        os.system(screen1_quit)
        os.system("echo $(date +%A-%m-%d-%Y_%H-%M-%S) \"Killed first screen\" >> $BORIKANES_HOME/deploy_log")

    os.system("cd $BORIKANES_HOME/node && screen -d -m npm start")
    os.system("cd $BORIKANES_HOME/flask && screen -d -m python3.4 flask_endpoints.py")
    os.system("echo $(date +%A-%m-%d-%Y_%H-%M-%S) \"Deploy Succesfull!\" >> $BORIKANES_HOME/deploy_log")
