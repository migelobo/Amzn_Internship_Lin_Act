from guizero import App, PushButton, Slider
import sys
import time
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

GPins = [27,17,22,18]

motortest = RpiMotorLib.BYJMotor("MotorOne","Nema")
time.sleep(.5)

def exitApp():
    sys.exit()

def motorF():
    motortest.motor_run(GPins, 0.001, 1120, True, False, "full",1)
def motorB():
    motortest.motor_run(GPins, 0.001, 1120, False, False, "full",1)
def eStop():
    motortest.motor_stop()
def breath():
    motortest.motor_run(GPins, 0.001, 1120, True, False, "full")
    motortest.motor_run(GPins, 0.001, 1120, False, False, "full")
    
app = App(layout="grid")

forwardButton = PushButton(app, motorF, text="Up", grid=[0,0])
forwardButton.text_size=36

backwardButton = PushButton(app, motorB, text="Down",grid=[0,1])
backwardButton.text_size=36

stopButton = PushButton(app, eStop, text="E-Stop", grid=[0,2])
stopButton.text_size=36

ABbutton = PushButton(app, breath, text="Breath", grid=[1,0])
ABbutton.text_size=36

exitButton = PushButton(app, exitApp, text="Exit", grid=[1,2])
exitButton.text_size=36

app.display()