# MQTT 패키지 설치 - paho-mqtt
# sudo pip install paho-mqtt
## 동시에 publish(데이터 전송[출판]) / subscribe(데이터 수신[구독]) 처리 

from threading import Thread, Timer
import time # time.sleep()
import json
import datetime as dt 

import paho.mqtt.client as mqtt

# DHT11 온습도센서 
import Adafruit_DHT as dht
#GPIO
import RPi.GPIO as GPIO

sensor = dht.DHT11
rcv_pin = 10
green = 22
servo_pin = 18

GPIO.setwarnings(False)     # 오류 메세지 제거

# green LED init
GPIO.setmode(GPIO.BCM)
GPIO.setup(green, GPIO.OUT)
GPIO.output(green, GPIO.HIGH)

#servo init
GPIO.setup (servo_pin, GPIO.OUT)    # servo init
pwm = GPIO.PWM(servo_pin, 50)
pwm.start(3)    # 각도 0도 DutyCycle 3~20


# 데이터를 보내는 쪽
class publisher(Thread):
    # 항상 생성
    def __init__(self):
        Thread.__init__(self)   # 스레드 초기화 
        self.host = '210.119.12.76' # 내 pc ip주소
        self.clientID = 'IOT76'
        self.port = 1883        # 회사에서는 이 포트 안씁니다. 
        print('publisher 스레드 시작')
        self.client = mqtt.Client(client_id= self.clientID)     # 설계대로
        self.count = 0
    # 실행함수
    def run (self):
        self.client.connect(self.host, self.port)
        # self.client.username_pw_set()   # dhtid/pwd로 로그인할때는 필요 
        self.publish_data_auto()

    def publish_data_auto(self):
        humid, temp = dht.read_retry(sensor, rcv_pin)
        curr = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 2023-06-14 10:39:24 이런식으로 변경
        origin_data = {'DEV_ID' : self.clientID,
                       'CURR_DT' : curr,
                       'TYPE' : 'TEMPHUMID',
                       'STAT': f'{temp} | {humid}'}    # real data로 변경 완 
        pub_data = json.dumps(origin_data)  # MQTT로 전송할 json데이터로 변환
        self.client.publish(topic='pknu/rpi/control/', payload=pub_data)
        print(f'Data published : {self.count}')
        self.count+=1
        Timer(2.0, self.publish_data_auto).start()  # 2초마다 출판

# 데이터를 받는쪽
class subscriber(Thread):
    def __init__(self):  # 생성자 
        Thread.__init__(self)
        self.host = '210.119.12.76' #broker ip
        self.port = 1883
        self.clientID='IOT76_SUB'
        self.topic = 'pknu/monitor/control/'
        print('subscriber 스레스 시작')
        self.client = mqtt.Client(client_id=self.clientID)

    def run(self):  # Thread.start() 함수를 실행하면 실행되는 함수
        self.client.on_connect = self.onConnect     # 접속이 성공 시그널 처리 
        self.client.on_message = self.onMessage     # 접속 후 메세지가 수신되면 그 다음을 처리 
        self.client.connect(self.host, self.port)
        self.client.subscribe(topic=self.topic)
        self.client.loop_forever()
    
    def onConnect(self, mqttc, obj, flags, rc):
        print(f'subscriber 연결됨 rc {rc}')

    def onMessage(self, mqttc, obj, msg):
        rcv_msg = str(msg.payload.decode('utf-8'))
        print(f'{msg.topic}/{rcv_msg}')
        data = json.loads(rcv_msg)
        stat = data['STAT']
        print(f'현재 STAT: {stat}')
        if (stat == 'OPEN'):
            GPIO.output(green, GPIO.LOW)
            pwm.ChangeDutyCycle(12)     # 90도
        elif (stat =='CLOSE'):
            GPIO.output(green, GPIO.HIGH)
            pwm.ChangeDutyCycle(3)      # 0도 

        time.sleep(1.0)


if __name__ == '__main__':
    thPub = publisher() # publisher 객체 생성
    thSub = subscriber()
    thPub.start() # run 자동 실행
    thSub.start() 

