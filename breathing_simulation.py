from guizero import App, TextBox, PushButton, ButtonGroup, Text
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
     breaths = int(breathText.value)
     steps = int(stepText.value)
     if steps>1120 or breaths<=0:
         return None
     for _ in range(breaths):
         oscillate(speed_value,steps)
def speed():
    speed = speedGroup.value
    if 'slow' in speed :
        speed_value = .1
    elif 'medium' in speed:
        speed_value = .01
    elif 'fast' in speed:
        speed_value = .001
    return speed_value
    
def run():
    breath(speed())
    
app = App('First Gui', height=400, width=300)
introText1 = Text(app, text="This will use a stepper motor to")
introText2 = Text(app, text="simulate breathing, please fill all")
introText3 = Text(app, text="text boxes before confirming.")
stepIntroText = Text(app, text="steps from 1 to 1120", size=10)
stepText = TextBox(app)
beathIntroText = Text(app, text="breaths to simulate greater than 0", size=10)
breathText = TextBox(app)
speedIntroText = Text(app, text="select a stepping rate", size=10)
speedGroup = ButtonGroup(app, options=["slow: 1 step every .1s", "medium: 1 step every .01s", "fast: 1 step every .001s"])
stepConfim = PushButton(app, command=run, text="Confim")

app.display()