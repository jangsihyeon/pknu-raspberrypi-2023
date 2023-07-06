import RPi.GPIO as GPIO
import time

a=9
b=10
c=3
d=27
e=17
f=5
g=11

i=0 # count

button = 4 

GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

GPIO.setup(a, GPIO.OUT)
GPIO.setup(b, GPIO.OUT)
GPIO.setup(c, GPIO.OUT)
GPIO.setup(d, GPIO.OUT)
GPIO.setup(e, GPIO.OUT)
GPIO.setup(f, GPIO.OUT)
GPIO.setup(g, GPIO.OUT)

try:
    while True:
        if GPIO.input(button)== GPIO.HIGH:
            i = i+1
            print(i)
            time.sleep(0.3)

        if(i==0):{
            GPIO.output(a, GPIO.LOW),
            GPIO.output(b, GPIO.LOW),
            GPIO.output(c, GPIO.LOW),
            GPIO.output(d, GPIO.LOW),
            GPIO.output(e, GPIO.LOW),
            GPIO.output(f, GPIO.LOW),
            GPIO.output(g, GPIO.LOW),
        }
        elif(i==1):{
            GPIO.output(a, GPIO.LOW),
            GPIO.output(b, GPIO.HIGH),
            GPIO.output(c, GPIO.HIGH),
            GPIO.output(d, GPIO.LOW),
            GPIO.output(e, GPIO.LOW),
            GPIO.output(f, GPIO.LOW),
            GPIO.output(g, GPIO.LOW),
        }
        elif(i==2):{
            GPIO.output(a, GPIO.HIGH),
            GPIO.output(b, GPIO.HIGH),
            GPIO.output(c, GPIO.LOW),
            GPIO.output(d, GPIO.HIGH),
            GPIO.output(e, GPIO.HIGH),
            GPIO.output(f, GPIO.LOW),
            GPIO.output(g, GPIO.HIGH),
        }
        elif(i==3):{
            GPIO.output(a, GPIO.HIGH),
            GPIO.output(b, GPIO.HIGH),
            GPIO.output(c, GPIO.HIGH),
            GPIO.output(d, GPIO.HIGH),
            GPIO.output(e, GPIO.LOW),
            GPIO.output(f, GPIO.LOW),
            GPIO.output(g, GPIO.HIGH),
        }
        elif(i==4):{
            GPIO.output(a, GPIO.LOW),
            GPIO.output(b, GPIO.HIGH),
            GPIO.output(c, GPIO.HIGH),
            GPIO.output(d, GPIO.LOW),
            GPIO.output(e, GPIO.LOW),
            GPIO.output(f, GPIO.HIGH),
            GPIO.output(g, GPIO.HIGH),
        }
        elif(i==5):{
            GPIO.output(a, GPIO.HIGH),
            GPIO.output(b, GPIO.LOW),
            GPIO.output(c, GPIO.HIGH),
            GPIO.output(d, GPIO.HIGH),
            GPIO.output(e, GPIO.LOW),
            GPIO.output(f, GPIO.HIGH),
            GPIO.output(g, GPIO.HIGH),
        }
        elif(i==6):{
            GPIO.output(a, GPIO.LOW),
            GPIO.output(b, GPIO.LOW),
            GPIO.output(c, GPIO.HIGH),
            GPIO.output(d, GPIO.HIGH),
            GPIO.output(e, GPIO.HIGH),
            GPIO.output(f, GPIO.HIGH),
            GPIO.output(g, GPIO.HIGH),
        }
        elif(i==7):{
            GPIO.output(a, GPIO.HIGH),
            GPIO.output(b, GPIO.HIGH),
            GPIO.output(c, GPIO.HIGH),
            GPIO.output(d, GPIO.LOW),
            GPIO.output(e, GPIO.LOW),
            GPIO.output(f, GPIO.HIGH),
            GPIO.output(g, GPIO.LOW),
        }
        elif(i==8):{
            GPIO.output(a, GPIO.HIGH),
            GPIO.output(b, GPIO.HIGH),
            GPIO.output(c, GPIO.HIGH),
            GPIO.output(d, GPIO.HIGH),
            GPIO.output(e, GPIO.HIGH),
            GPIO.output(f, GPIO.HIGH),
            GPIO.output(g, GPIO.HIGH),
        }   
        elif(i==9):{
            GPIO.output(a, GPIO.HIGH),
            GPIO.output(b, GPIO.HIGH),
            GPIO.output(c, GPIO.HIGH),
            GPIO.output(d, GPIO.LOW),
            GPIO.output(e, GPIO.LOW),
            GPIO.output(f, GPIO.HIGH),
            GPIO.output(g, GPIO.HIGH),
        }   
        elif(i==10):{
            GPIO.output(a, GPIO.HIGH),
            GPIO.output(b, GPIO.HIGH),
            GPIO.output(c, GPIO.HIGH),
            GPIO.output(d, GPIO.LOW),
            GPIO.output(e, GPIO.HIGH),
            GPIO.output(f, GPIO.HIGH),
            GPIO.output(g, GPIO.HIGH),
        }   
        elif(i==11):{
            GPIO.output(a, GPIO.HIGH),
            GPIO.output(b, GPIO.HIGH),
            GPIO.output(c, GPIO.HIGH),
            GPIO.output(d, GPIO.HIGH),
            GPIO.output(e, GPIO.HIGH),
            GPIO.output(f, GPIO.HIGH),
            GPIO.output(g, GPIO.HIGH),
        }   
        elif(i==12):{
            GPIO.output(a, GPIO.HIGH),
            GPIO.output(b, GPIO.LOW),
            GPIO.output(c, GPIO.LOW),
            GPIO.output(d, GPIO.HIGH),
            GPIO.output(e, GPIO.HIGH),
            GPIO.output(f, GPIO.HIGH),
            GPIO.output(g, GPIO.LOW),
        }   
        elif(i==13):{
            GPIO.output(a, GPIO.HIGH),
            GPIO.output(b, GPIO.HIGH),
            GPIO.output(c, GPIO.HIGH),
            GPIO.output(d, GPIO.HIGH),
            GPIO.output(e, GPIO.HIGH),
            GPIO.output(f, GPIO.HIGH),
            GPIO.output(g, GPIO.LOW),
        }   
        elif(i==14):{
            GPIO.output(a, GPIO.HIGH),
            GPIO.output(b, GPIO.LOW),
            GPIO.output(c, GPIO.LOW),
            GPIO.output(d, GPIO.HIGH),
            GPIO.output(e, GPIO.HIGH),
            GPIO.output(f, GPIO.HIGH),
            GPIO.output(g, GPIO.HIGH),
        }   
        elif(i==15):{
            GPIO.output(a, GPIO.HIGH),
            GPIO.output(b, GPIO.LOW),
            GPIO.output(c, GPIO.LOW),
            GPIO.output(d, GPIO.LOW),
            GPIO.output(e, GPIO.HIGH),
            GPIO.output(f, GPIO.HIGH),
            GPIO.output(g, GPIO.HIGH),
        }
except KeyboardInterrupt:
    print("완료")
    GPIO.cleanup()