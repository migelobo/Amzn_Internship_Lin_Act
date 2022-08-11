#all the imort used in this program
from re import A
from urllib import request
from bottle import *
import time
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

#this line is used only if we are movment2 function as opposed to movement1
#make sure to uncomment if using movement2 and recomment if going back to movement1
#GPIO.setmode(GPIO.BOARD)

#these are the globabl vaiables created to be updated later in the program to be
#displayed on website
global time_lp,temp,steps
temp = True
time_lp = 0
steps = 0
#variable names for the pin order number on the raspberry pi used for direction
#in program. fs for full step; hs for half step. These are only used in movement2
fs_revGPins = [12,13,11,15]
fs_GPins = [15,11,13,12]

hs_revGPins = [13,11,15,12]
hs_GPins = [12,15,11,13]

#the GPIO pins on the raspberrypi used for movement1 funcion
#comment out if using movement2
GPins = [27,17,22,18]

#this line utilizes the RpiMotorLib import to assign Stepper Motor functions to a variable
motortest = RpiMotorLib.BYJMotor("MotorOne","Nema")
#the ip address used for the web server to be created
HOST = '192.168.35.213'

#function to convert time to be displayed on website
def time_convert(sec):
    mins = sec//60
    sec = sec%60
    hours = mins//60
    mins = mins%60
    return "{0}:{1}".format(int(mins),round(sec,2))

#function for setting pin values to move forward for full step
def fs_forward():
    GPins = fs_GPins
    #initializes pin values to 0
    for pin in GPins:
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin,0)
    return GPins
#function for setting pin values to move backward for full step
def fs_backward():
    GPins = fs_revGPins
    #initializes pin values to 0
    for pin in GPins:
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin,0)
    return GPins
#function for setting pin values to move forward for half step
def hs_forward():
    GPins = hs_GPins
    for pin in GPins:
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin,0)
    return GPins
#function for setting pin values to move backward for full step
def hs_backward():
    GPins = hs_revGPins
    for pin in GPins:
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin,0)
    return GPins

#the order in which the electromagnets in the stepper motor activate via the GPIO pin connections
#the first is the full step sequence, the second the half step one. This is used explicitly in 
#movement2 function but implicitly in movement1
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
    
#function for moving the stepper motor in a certian direction based on steps, and rpm but used
#other inputs to differentiate between what direction and type is wanted
def movement2(stepCount,count,pin_order,seq,base,rpm):
    #for loop for amount of steps to take
    for i in range(stepCount):
            #sequence of drive to be used depending o step type
            for step_type in range(count):
                #cycle through all 4 GPIO pins in the specified sequence order
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

#this is for the format and style of the website to find CSS files used
#@route, routes the website to that 
@route('/static/<filepath:path>')
def serve_files(filepath):
    return static_file(filepath, root='/home/pi/Linear_Actuator/static')

#routes website to homepage and displays steps and time lapsed if variables were found 
@route('/')
def index():
    
    if temp:
        time_lapse = 0
        steps_oscillated = 0
    else:
        time_lapse = time_lp
        steps_oscillated = steps
    #this data is what us reference in the HTML code 
    my_data = {
        'time_lapse': time_lapse,
        'steps_oscillated': steps_oscillated
        }
    print(time_lp)
    #returns the template of the HTML page we created and displays the data we gathered if it is available
    return template('/home/pi/Linear_Actuator/main.tpl', **my_data)

#function that routes from main website to loading screen to run the stepper motor code
@route('/Stepper_motor', method='POST')
def Stepper_motor():
    #gets all the values imputed in the breathing section of the website to be converted to usable variables
    amplitude = int(request.forms.get('amplitude'))
    rpm = float(request.forms.get('rpm'))
    breaths = int(request.forms.get('number_breaths'))
    #converts mm input to step
    stepCount = 10*amplitude
    #equation that allows us to utilize both the wanted rpm and step count to make the the stepper motor speed revolve at the 
    #proper speed for the inputed RPM
    rev_per_min = stepCount*(.04)*rpm
    #these variables are utilized when using movement2
    count = 8
    pin_order = hs_forward()
    rev_pin_order = hs_backward()
    seq = half_step()
    #variables utilzed to make the motor move in half step mode for accurate detection
    stepType = 0
    base = .0375
    direction=1
    revdirection=0
    #global variables that are updted for when we redirect back to main website after code is ran
    global temp
    temp = False
    global time_lp
    global steps
    #starts timer to know total time spent in loop
    start_time = time.time()
    #repeats the breathing based on user input
    for number in range(breaths):
        movement1(stepCount,direction,stepType,base,rev_per_min)
        movement1(stepCount,revdirection,stepType,base,rev_per_min)    
        #movement2(stepCount,count,pin_order,seq,base,rev_per_min)
        #movement2(stepCount,count,rev_pin_order,seq,base,rev_per_min)
    #timer end to display
    end_time = time.time()
    time_lp = time_convert(end_time-start_time)
    steps = stepCount
    #redirects to the @route("/") function were new values are upated and you are retuned to main page
    redirect("/")
#function that routes from main website to loading sreen when running the debugging code
@route('/Debug_Stepper', method='POST')
def Debug_stepper():
    #gets all the values inputed in the debugging section of the website to be converted to usable variables
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
    #checks if breathing was selected to be turned on
    if checkbox:
        breaths = request.forms.get('number_breaths')
        breaths = int(breaths)
    else:
        breaths = None 
    
    #a check of all the values to set the arguments for movement code to whatever user inputted
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
    #equation for speed needed to get accurate RPM
    rev_per_min = stepCount*(.04)*rpm

    #global variables that are updted for when we redirect back to main website after code is ran
    global temp
    temp = False
    global time_lp
    
    #check to see if breaths was activated and how many times movemen code is needed to run
    if breaths == None:
        #starts timer to know total time spent moving
        start_time = time.time()
        #movement2(stepCount,count,pin_order,seq,base,rev_per_min)
        movement1(stepCount,direction,stepType,base,rpm)
        end_time = time.time()
        time_lp = time_convert(end_time-start_time)
    elif breaths != None:
        start_time = time.time()
        for number in range(breaths):
            movement1(stepCount,direction,stepType,base,rev_per_min)
            movement1(stepCount,revdirection,stepType,base,rev_per_min)
            #movement2(stepCount,count,pin_order,seq,base,rev_per_min)
            #movement2(stepCount,count,rev_pin_order,seq,base,rev_per_min)
        end_time = time.time()
        time_lp = time_convert(end_time-start_time)
    #redirects to the @route("/") function were new values are upated and you are retuned to main page
    redirect("/")

#launches the website based on host name
run(host=HOST, port=80, debug=True, reloader=True)
