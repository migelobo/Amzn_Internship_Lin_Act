from guizero import App, TextBox, PushButton, ButtonGroup
import sys
import time
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

GPins = [27,17,22,18]

motortest = RpiMotorLib.BYJMotor("MotorOne","Nema")
time.sleep(.5)

def exitApp():
    sys.exit()
def motorF(speed_value, step_value):
    motortest.motor_run(GPins, speed_value, step_value, True, False, "full")
def motorB(speed_value, step_value):
    motortest.motor_run(GPins, speed_value, step_value, False, False, "full")
def oscillate(speed_value, step_value):
    motortest.motor_run(GPins, speed_value, step_value, True, False, "full")
    motortest.motor_run(GPins, speed_value, step_value, False, False, "full")

def step():
    x = int(stepText.value)
    if x>0:
        motorF(x)
    elif x<0:
        x = x*-1
        motorB(x)
def breath(speed_value):
     y = int(breathText.value)
     z = int(stepText.value)
     if z>1120:
         return None
     for _ in range(y):
         oscillate(speed_value,z)
def speed():
    speed = speedGroup.value
    if speed in ['slow']:
        speed_value = .1
    elif speed in ['medium']:
        speed_value = .01
    elif speed in ['fast']:
        speed_value = .001
    return speed_value
    
def run():
    breath(speed())
    
app = App('First Gui', height=400, width=300)
stepText = TextBox(app)
breathText = TextBox(app)
speedGroup = ButtonGroup(app, options=["slow", "medium", "fast"])
stepConfim = PushButton(app, command=run, text="Confim")
#breathConfim = PushButton(app, commaSnd=breath, text="Confim")




app.display()