# LED 깜빡이기 
import RPi.GPIO as GPIO
import time

is_run = True
red = 17
green = 27
blue = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

try:
    while True:
        GPIO.output(red, True)
        GPIO.output(blue, False)
        GPIO.output(green, False)
        time.sleep(5)
        GPIO.output(red, False)
        GPIO.output(green, True)
        GPIO.output(blue, False)
        time.sleep(5)
        GPIO.output(green, False)
        GPIO.output(red, False)
        GPIO.output(blue, True)
        time.sleep(5)
        
except KeyboardInterrupt:
    GPIO.cleanup()