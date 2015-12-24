#!/bin/bash

sleep 2
cd $BORIKANES_HOME && git pull origin master
cd $BORIKANES_HOME/node && npm install
cd $BORIKANES_HOME/flask && pip3 install -r requirements.txt 
