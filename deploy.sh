#!/bin/bash
# screen -X -S 3060.ttys000.34363bd1bda6 quit
# ps aux |grep -v "grep" | grep "node ./app.js"

# ps_output=`ps aux |grep -v "grep" | grep "node ./app.js" | awk '{print $6}'`
SCREEN_PROCESS=`screen -list | awk '{print $1}' | grep "\.\."`
# FIRST_SCREEN_PROCESS=`screen -list | awk '{print $1}' | grep "\.\."  | sed -n 1p` # gets the first screen process
# SECOND_SCREEN_PROCESS=`screen -list | awk '{print $1}' | grep "\.\."  | sed -n 2p` # gets second screen process

if [ ! "$SCREEN_PROCESS" ]; then
  echo $(date +%A-%m-%d-%Y_%H-%M-%S) "No screen sessions" >> /home/pi/Code/borikanes/deploy_log
  exit
else
  screen -ls | grep Detached | cut -d. -f1 | awk '{print $1}' | xargs kill
  cd $BORIKANES_HOME && git pull origin master
  cd $BORIKANES_HOME/node && screen -d -m npm start && cd $BORIKANES_HOME/flask && screen -d -m python3.4 flask_endpoints.py
  echo $(date +%A-%m-%d-%Y_%H-%M-%S) "Deploy Succesfull!" >> /home/pi/Code/borikanes/deploy_log
fi
