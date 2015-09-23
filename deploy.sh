#!/bin/bash
# screen -X -S 3060.ttys000.34363bd1bda6 quit
# ps aux |grep -v "grep" | grep "node ./app.js"

ps_output=`ps aux |grep -v "grep" | grep "node ./app.js" | awk '{print $6}'`
SCREEN_PROCESS=`screen -list | awk '{print $1}' | grep "tty"`

if [ ! $SCREEN_PROCESS ]; then
  echo $(date +%A-%m-%d-%Y_%H-%M-%S) "No screen sessions" >> deploy_log
  exit
else
  screen -X -S $SCREEN_PROCESS quit #kills screen process
  cd ~/Code/borikanes && git pull origin autodeploy-shellscript
  # /home/pi/Code/borikanes
fi
