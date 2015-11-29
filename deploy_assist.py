import sys
import os
import subprocess

# first_process = "screen -list | awk '{print $1}' | grep \"\.\.\"  | sed -n 1p"
# second_process = "screen -list | awk '{print $1}' | grep \"\.\.\"  | sed -n 2p"

first_process = os.popen('screen -list | awk \'{print $1}\' | grep \"\.\.\"  | sed -n 1p') # gets the first screen process
second_process = os.popen('screen -list | awk \'{print $1}\' | grep \"\.\.\"  | sed -n 2p') # gets second screen process
screen1 = str(first_process.read()).rstrip('\n')
screen2 = str(second_process.read()).rstrip('\n')

os.system("echo $(date +%A-%m-%d-%Y_%H-%M-%S) \"Else statement\" >> /home/pi/Code/borikanes/deploy_log")
os.system("cd /home/pi/Code/borikanes && git pull origin master")

if(first_process):
    os.system("screen -X -S $FIRST_SCREEN_PROCESS quit")
    os.system("echo $(date +%A-%m-%d-%Y_%H-%M-%S) \"Killed first screen\" >> /home/pi/Code/borikanes/deploy_log")
if(second_process):
    os.system("screen -X -S $SECOND_SCREEN_PROCESS quit")
    os.system("echo $(date +%A-%m-%d-%Y_%H-%M-%S) \"Killed second screen\" >> /home/pi/Code/borikanes/deploy_log")

os.system("cd /home/pi/Code/borikanes/node && screen -d -m npm start && cd /home/pi/Code/borikanes/flask && screen -d -m python3.4 flask_endpoints.py")
os.system("echo $(date +%A-%m-%d-%Y_%H-%M-%S) \"Deploy Succesfull!\" >> /home/pi/Code/borikanes/deploy_log")
