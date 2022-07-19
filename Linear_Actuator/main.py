from bottle import *
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPins = [12,11,13,15]
revGPins = [15,13,11,12]


HOST = '192.168.35.213'

seq = [[1,1,0,0],
       [0,1,1,0],
       [0,0,1,1],
       [1,0,0,1]]

for pin in GPins:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,0)

rotationNeeded=0
rotationCount=0

@route('/')
def index():
    return template('/home/pi/Linear_Actuator/main.tpl')


@route('/Stepper_motor', method='POST')
def Stepper_motor():
    stepCount = request.forms.get('steps')
    rpm = request.forms.get('rpm')
    stepCount = int(stepCount)
    rpm = rpm = int(rpm)
    count = 4
    base = .075
    
    for i in range(stepCount):
        for step_type in range(count):
            for pin in range(4):
                GPIO.output(GPins[pin],seq[step_type][pin])
                time.sleep(base/rpm)
    redirect("/")

    
run(host=HOST, port=80, debug=True, reloader=True)