#!/bin/bash
# screen -X -S 3060.ttys000.34363bd1bda6 quit
# ps aux |grep -v "grep" | grep "node ./app.js"

ps_output=`ps aux |grep -v "grep" | grep "node ./app.js" | awk '{print $6}'`
SCREEN_PROCESS=`screen -list | awk '{print $1}' | grep "tty"`

if [ $SCREEN_PROCESS ]; then
  screen -X -S $SCREEN_PROCESS quit #kills screen process
else
  echo "No screen sessions yet"
fi
# else
#   echo "Screen was not running" >> /var/log/deploy_logs
