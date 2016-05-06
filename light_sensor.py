#!/usr/bin/env python

# importing the GPIO library
# for reading input and handling output 
# importing time and os
import RPi.GPIO as GPIO, time, os

DEBUG = 1
GPIO.setmode(GPIO.BCM)

# defining the RCtime function
def RCtime (RCpin):
        reading = 0

        GPIO.setup(RCpin, GPIO.OUT)
        GPIO.output(RCpin, GPIO.LOW)
	# sleeping for a tenth of a second so the computer is not overwhelmed
        time.sleep(0.1)

        GPIO.setup(RCpin, GPIO.IN)

        # this takes about 1 millisecond per loop cycle
        while (GPIO.input(RCpin) == GPIO.LOW):
                reading += 1
        return reading

# calling and printing the output of the RCtime funtion
print RCtime(18)     # Read RC timing using pin #18

