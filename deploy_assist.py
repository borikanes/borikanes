import sys
import os
import subprocess

screen_process = os.popen('screen -list | awk \'{print $1}\' | grep "\.\."')
screen_process_clean = str(screen_process.read()).rstrip('\n')
if(not screen_process_clean):
    os.system("echo $(date +%A-%m-%d-%Y_%H-%M-%S) \"No screen sessions\" >> ~/Code/borikanes/deploy_log && exit")
else:
    first_process = os.popen('screen -list | awk \'{print $1}\' | grep \"\.\.\"  | sed -n 1p') # gets the first screen process
    second_process = os.popen('screen -list | awk \'{print $1}\' | grep \"\.\.\"  | sed -n 2p') # gets second screen process
    screen1 = str(first_process.read()).rstrip('\n')
    screen2 = str(second_process.read()).rstrip('\n')

    os.system("echo $(date +%A-%m-%d-%Y_%H-%M-%S) \"Else statement\" >> ~/Code/borikanes/deploy_log")
    os.system("cd ~/Code/borikanes && git pull origin master")

    screen1_quit = "screen -X -S "+screen1+" quit"
    screen2_quit = "screen -X -S "+screen2+" quit"

    if(first_process):
        os.system(screen1_quit)
        os.system("echo $(date +%A-%m-%d-%Y_%H-%M-%S) \"Killed first screen\" >> ~/Code/borikanes/deploy_log")
    if(second_process):
        os.system(screen2_quit)
        os.system("echo $(date +%A-%m-%d-%Y_%H-%M-%S) \"Killed second screen\" >> ~/Code/borikanes/deploy_log")

    os.system("cd ~/Code/borikanes/node && screen -d -m npm start")
    os.system("cd ~/Code/borikanes/flask && screen -d -m python3.4 flask_endpoints.py")
    os.system("echo $(date +%A-%m-%d-%Y_%H-%M-%S) \"Deploy Succesfull!\" >> ~/Code/borikanes/deploy_log")
