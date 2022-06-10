import time
import RPi.GPIO as GPIO

from RpiMotorLib import RpiMotorLib

GPins = [27,17,22,18]

motortest = RpiMotorLib.BYJMotor("MotorOne","Nema")
time.sleep(.5)
#motor_run(GPIOPins, wait, steps, ccw, verbose,steptype,initdelay)

motortest.motor_run(GPins, 0.001, 1120, True, False, "full",.1)
#motortest.motor_run(GPins, 0.001, 1120, False, False, "half", .05)

#except KeyboardInterrupt:
GPIO.cleanup()