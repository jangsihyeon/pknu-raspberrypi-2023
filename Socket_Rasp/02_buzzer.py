import RPi.GPIO as GPIO
import time

buzzerpin = 13
melody =[131,147,165,175,196,220,247,262]
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzerpin, GPIO.OUT)

buzz = GPIO.PWM(buzzerpin, 440)

try:
    while True:
        buzz.start(50)
        for i in range(0, len(melody)):
            buzz.ChangeFreqency(melody[i])
            time.sleep(0.3)
        buzz.stop()
        time.sleep(1)

except KeyboardInterrupt:
    print("소리 센서 완")
    GPIO.cleanup()