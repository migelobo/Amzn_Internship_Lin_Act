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
    
def motorF(rpm,steps):
    motortest.motor_run(GPins, (.3/rpm), steps, True, False, "full")

def motorB(rpm,steps):
    motortest.motor_run(GPins, (.3/rpm), steps, False, False, "full")
    
def osscilate(rpm,steps):
    motorF(rpm,steps)
    motorB(rpm,steps)
    
def step_run():
    rpm = int(rpmText.value)
    steps = int(stepText.value)
    if steps > 0:
        motorF(rpm,steps)
    elif steps < 0:
        steps= steps*-1
        motorB(rpm,steps)

def breath_run():
    rpm = int(rpmText.value)
    steps = int(stepText.value)
    breaths = int(breathsText.value)
    if steps > 0:
        for breath in range(breaths):
            motorF(rpm,steps)
            motorB(rpm,steps)
    elif steps < 0:
        steps= steps*-1
        for breath in range(breaths):
            motorB(rpm,steps)
            motorF(rpm,steps)

app = App('First Gui', height=400, width=300)

stepText = TextBox(app)
stepIntroText = Text(app, text="Steps", size=10)

rpmText = TextBox(app)
rpmIntroText = Text(app, text="RPM", size=10)

breathsText = TextBox(app)
breathsIntroText = Text(app, text="Breaths", size=10)

stepConfirm = PushButton(app, command=step_run, text="Step Movemnt")
breahConfirm = PushButton(app, command= breath_run, text="Breathing Movement")
app.display()
GPIO.cleanup()