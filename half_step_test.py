import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

pin_order = [12,13,11,15]

seq =  [[1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,0,1],
        [1,0,0,1]]

def time_convert(sec):
    mins = sec//60
    sec = sec%60
    hours = mins//60
    mins = mins%60
    print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))


for pin in pin_order:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,0)

start_time = time.time()
for i in range(50):
    for step_type in range(4):
        for pin in range(4):
            GPIO.output(pin_order[pin],seq[step_type][pin])
            time.sleep(.01)
end_time = time.time()
time_convert(end_time-start_time)
GPIO.cleanup()
