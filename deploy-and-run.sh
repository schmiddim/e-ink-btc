#!/bin/bash
HOST=pandadisplay
REMOTE_PATH=/home/pi/e-ink-btc
scp display.py  $HOST:$REMOTE_PATH
scp -r * $HOST:$REMOTE_PATH
ssh $HOST "python3 $REMOTE_PATH/display.py"
