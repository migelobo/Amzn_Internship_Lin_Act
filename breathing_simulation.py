#imports for gui, steppermotor, and GPIO please refer to links for more info
#Stepper Motor Info: https://github.com/gavinlyonsrepo/RpiMotorLib
#GUI Info: https://lawsie.github.io/guizero/
from guizero import App, TextBox, PushButton, ButtonGroup, Text
import sys
import time
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

#GPIOfor IN3,IN2,IN4,IN1
GPins = [27,17,22,18]

#variable name for stepper motor along with its type
motortest = RpiMotorLib.BYJMotor("MotorOne","Nema")
time.sleep(.5)

#function to exit gui
def exitApp():
    sys.exit()
#function to move stepper forward
def motorF(speed_value, step_value):
    motortest.motor_run(GPins, speed_value, step_value, True, False, "full")
#function to move stepper backward
def motorB(speed_value, step_value):
    motortest.motor_run(GPins, speed_value, step_value, False, False, "full")
#function to oscillate stepper
def oscillate(speed_value, step_value):
    motortest.motor_run(GPins, speed_value, step_value, False, False, "full")
    motortest.motor_run(GPins, speed_value, step_value, True, False, "full")
#function to move stepper forward/backward based on gui input
def step():
    x = int(stepText.value)
    if x>0:
        motorF(x)
    elif x<0:
        x = x*-1
        motorB(x)
#function to simulate breathing based in gui inputs for speed, steps, and "breaths" (oscillations)
def breath(speed_value):
     breaths = int(breathText.value)
     steps = int(stepText.value)
     if steps>1120 or breaths<=0:
         return None
     for _ in range(breaths):
         oscillate(speed_value,steps)
#function to determine stepper motor speed based on gui input
def speed():
    speed = speedGroup.value
    if 'slow' in speed :
        speed_value = .1
    elif 'medium' in speed:
        speed_value = .01
    elif 'fast' in speed:
        speed_value = .002
    return speed_value
#function to run all previous functions once confirm button is pressed
def run():
    breath(speed())

#initializtion of gui size and placements for text, textboxes, and buttons
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
#displays the gui in a window
app.display()