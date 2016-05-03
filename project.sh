#!/bin/bash

control_c() {
        kill $PID
}

trap control_c SIGINT

while true; do

        python ./light_sensor.py

        if [ $( python ./light_sensor.py  ) -ge 100000 ]
        then    python ./snap_photo.py
                python ./send_email4.py
                PID=$!
                fi
done

