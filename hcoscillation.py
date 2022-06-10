import time
import RPi.GPIO as GPIO

from RpiMotorLib import RpiMotorLib

GPins = [27,17,22,18]

motortest = RpiMotorLib.BYJMotor("MotorOne","Nema")
time.sleep(.5)

while(1):
    motortest.motor_run(GPins, 0.001, 1120, True, False, "full")
    motortest.motor_run(GPins, 0.001, 1120, False, False, "full")

GPIO.cleanup()
