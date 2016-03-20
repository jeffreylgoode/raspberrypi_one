import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup (27, GPIO.OUT)

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
