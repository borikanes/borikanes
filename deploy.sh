#!/bin/bash
# screen -X -S 3060.ttys000.34363bd1bda6 quit
# ps aux |grep -v "grep" | grep "node ./app.js"

ps_output=`ps aux |grep -v "grep" | grep "node ./app.js" | awk '{print $6}'`
screen_process=`screen -list | awk '{print $1}' | grep "tty"`
echo $screen_process
# if [ $ps_output == "26568" ]; then
#   echo "it worked"
# fi
