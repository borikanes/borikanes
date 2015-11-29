#!/bin/bash
# screen -X -S 3060.ttys000.34363bd1bda6 quit
# ps aux |grep -v "grep" | grep "node ./app.js"

ps_output=`ps aux |grep -v "grep" | grep "node ./app.js" | awk '{print $6}'`
SCREEN_PROCESS=`screen -list | awk '{print $1}' | grep "\.\."`
FIRST_SCREEN_PROCESS=`screen -list | awk '{print $1}' | grep "\.\."  | sed -n 1p` # gets the first screen process
SECOND_SCREEN_PROCESS=`screen -list | awk '{print $1}' | grep "\.\."  | sed -n 2p` # gets second screen process

if [ ! "$SCREEN_PROCESS" ]; then
  echo $(date +%A-%m-%d-%Y_%H-%M-%S) "No screen sessions" >> deploy_log
  exit
else
  echo "Else statement" >> deploy_log
  if [ "$FIRST_SCREEN_PROCESS" ]; then
    screen -X -S $FIRST_SCREEN_PROCESS quit #kills first screen process
    echo "Killed first screen" >> deploy_log
  fi
  if [ "$SECOND_SCREEN_PROCESS" ]; then
    screen -X -S $SECOND_SCREEN_PROCESS quit #kills second screen process
    echo "Killed second screen" >> deploy_log
  fi
  echo "Got through" >> deploy_log
  cd /home/pi/Code/borikanes && git pull origin master
  cd /home/pi/Code/borikanes/node && screen -d -m npm start
  cd /home/pi/Code/borikanes/flask && screen -d -m python3.4 flask_endpoints.py
  echo $(date +%A-%m-%d-%Y_%H-%M-%S) "Deploy Succesfull!" >> deploy_log
fi
