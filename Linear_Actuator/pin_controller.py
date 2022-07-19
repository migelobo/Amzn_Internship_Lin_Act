import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
import time

GPIO.setmode(GPIO.BOARD)

GPins = [12,11,13,15]
revGPins = [15,13,11,12]
#pins = [{'pin number': 27, 'wire': ''},
#       {'pin number': 17, 'wire': ''},
#      {'pin number': 22, 'wire': ''},
#        {'pin number': 18, 'wire': ''}]

for pin in revGPins:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,0)

rotationNeeded=0
rotationCount=0


def time_convert(sec):
    mins = sec//60
    sec = sec%60
    hours = mins//60
    mins = mins%60
    print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))


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


def forward():
    GPins = [12,11,13,15]
    return GPins
def backward():
    GPins = [15,13,11,12]
    return GPins


def movement(steps,rpm,direction,stepType):
    if direction == 'f':
        pin_order = forward()
    elif direction == 'b':
        pin_order = backward()
        
    if stepType == 'fs':
        seq = full_step()
        base = .075
        count = 4
    elif stepType == 'hs':
        seq = half_step()
        base = .0375
        count = 8
    
    rpm = rpm
    stepCount=steps
    start_time = time.time()
    
    for i in range(stepCount):
        for step_type in range(count):
            for pin in range(4):
                GPIO.output(pin_order[pin],seq[step_type][pin])
                time.sleep(base/rpm)
    end_time = time.time()
    time_convert(end_time-start_time)

while(1):
    rotationNeeded==0
    print("\n")
    stepType = input("press e-exit,\nfs - full step\nhs - half step: ")
    steps=int(input("How many steps needed..."))
    rpm = int(input("How many RPM: "))
    direction = input("f - forward \nb - backwards: ")
    print("\n")
    if steps=='e':
        break

    movement(steps,rpm,direction,stepType)          
    
GPIO.cleanup()