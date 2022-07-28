from bottle import *
import time
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

GPIO.setmode(GPIO.BOARD)

global time_lp,temp
temp = True
time_lp = 0

fs_revGPins = [12,13,11,15]
fs_GPins = [15,11,13,12]

hs_revGPins = [13,11,15,12]
hs_GPins = [12,15,11,13]
GPins = [27,17,22,18]

# motortest = RpiMotorLib.BYJMotor("MotorOne","Nema")
HOST = '192.168.35.213'

def time_convert(sec):
    mins = sec//60
    sec = sec%60
    hours = mins//60
    mins = mins%60
    return "{0}:{1}".format(int(mins),round(sec,2))


def fs_forward():
    GPins = fs_GPins
    
    for pin in GPins:
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin,0)
    return GPins

def fs_backward():
    GPins = fs_revGPins
    for pin in GPins:
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin,0)
    return GPins
def hs_forward():
    GPins = hs_GPins
    for pin in GPins:
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin,0)
    return GPins
def hs_backward():
    GPins = hs_revGPins
    for pin in GPins:
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin,0)
    return GPins

def full_step():
    seq = [[1,1,0,0],
           [0,1,1,0],
           [0,0,1,1],
           [1,0,0,1]]
    return seq
def half_step():
    seq =  [[1,0,0,0],
            [1,1,0,0],
            [0,1,0,0],
            [0,1,1,0],
            [0,0,1,0],
            [0,0,1,1],
            [0,0,0,1],
            [1,0,0,1]]  
    return seq
    
def movement2(stepCount,count,pin_order,seq,base,rpm):

    for i in range(stepCount):
            for step_type in range(count):
                for pin in range(4):
                    GPIO.output(pin_order[pin],seq[step_type][pin])
                    time.sleep(base/rpm)

def movement1(stepCount,direction,stepType,base,rpm):
    if base == .075:
        base = .3
    elif base == .0375:
        base = .15

    if direction == 1:
        if stepType == 1:
            motortest.motor_run(GPins, (base/rpm), stepCount, True, False, "full")
        elif stepType ==0:
            motortest.motor_run(GPins, (base/rpm), stepCount, True, False, "half")
    elif direction == 0:
        if stepType == 1:
            motortest.motor_run(GPins, (base/rpm), stepCount, False, False, "full")
        elif stepType == 0:    
            motortest.motor_run(GPins, (base/rpm), stepCount, False, False, "half")
@route('/static/<filepath:path>')
def serve_files(filepath):
    return static_file(filepath, root='/home/pi/Linear_Actuator/static')


@route('/')
def index():
    
    if temp:
        time_lapse = 0
    else:
        time_lapse = time_lp
    
    my_data = {
        'time_lapse': time_lapse
        }
    print(time_lp)
    return template('/home/pi/Linear_Actuator/main.tpl', **my_data)


@route('/Stepper_motor', method='POST')
def Stepper_motor():
    stepCount = request.forms.get('steps')
    rpm = request.forms.get('rpm')
    stepType = request.forms.get('step_type')
    direction = request.forms.get('direction')
    checkbox = request.forms.get('breathe')
    
    checkbox = bool(checkbox)
    stepCount = int(stepCount)
    rpm = rpm = float(rpm)
    stepType = int(stepType)
    direction = int(direction)
    
    if checkbox:
        breaths = request.forms.get('number_breaths')
        breaths = int(breaths)
    else:
        breaths = None
    
    
    if direction == 1:
        revdirection = 0
        if stepType == 1:
            pin_order = fs_forward()
            rev_pin_order = fs_backward()
            seq = full_step()
            base = .075
            count = 4
        elif stepType ==0:
            pin_order = hs_forward()
            rev_pin_order = hs_backward()
            seq = half_step()
            base = .0375
            count = 8
    elif direction == 0:
        revdirection = 1
        if stepType ==1:
            pin_order = fs_backward()
            rev_pin_order = fs_forward()
            seq = full_step()
            base = .075
            count = 4
        elif stepType == 0:
            pin_order = hs_backward()
            rev_pin_order = hs_forward()
            seq = half_step()
            base = .0375
            count = 8
    global temp
    temp = False
    global time_lp
    if breaths == None:
        start_time = time.time()
        movement2(stepCount,count,pin_order,seq,base,rpm)
        # movement1(stepCount,direction,stepType,base,rpm)
        end_time = time.time()
        time_lp = time_convert(end_time-start_time)
    elif breaths != None:
        for number in range(breaths):
            start_time = time.time()
            # movement1(stepCount,direction,stepType,base,rpm)
            # movement1(stepCount,revdirection,stepType,base,rpm)
            movement2(stepCount,count,pin_order,seq,base,rpm)
            movement2(stepCount,count,rev_pin_order,seq,base,rpm)
            end_time = time.time()
            time_lp = time_convert(end_time-start_time)
    redirect("/")

    
run(host=HOST, port=80, debug=True, reloader=True)
