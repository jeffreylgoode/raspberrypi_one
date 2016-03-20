# my first Raspberry Pi code
# this is the LED version of hello world
# I purchased bread board, resistors, jumpers and LEDs from Gigaparts

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT) # Green LED
GPIO.setup (27, GPIO.OUT) # Red LED

# Alternate red and green LEDs on and off, on and off time is 0.5 seconds

while True:
    GPIO.output(17,1)
    GPIO.output(27,0)
    time.sleep(0.5)
    GPIO.output(17,0)
    GPIO.output(27,1)
    time.sleep(0.5)
    
GPIO.cleanup(17)
GPIO.cleanup(27)
print GPIO.RPI_INFO
print GPIO.VERSION
