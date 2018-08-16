

'''
Modified Raspberry Pi Stepper Motor Tutorial setup and code,
rdagger68, to control 3 stepper motors
'''


from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

xDIR = 20   # Direction GPIO Pin
xSTEP = 21  # Step GPIO Pin

yDIR = 19
ySTEP = 26

zDIR = 6
zSTEP = 13

CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation

xSPR = 48   # Steps per Revolution (360 / 7.5) 
ySPR = 48   # Less Distance
zSPR = 148  # Greater Distance

GPIO.setwarnings(False)

xSPR = input("Select Steps per Revolution: (24-120)") # z stage
print("Steps per Revolution: ", xSPR)

ySPR = input("Select Steps per Revolution: (24-120)") # z stage
print("Steps per Revolution: ", ySPR)

zSPR = input("Select Steps per Revolution: (24-120)") # z stage
print("Steps per Revolution: ", zSPR)


GPIO.setup(xDIR, GPIO.OUT)
GPIO.setup(xSTEP, GPIO.OUT)
GPIO.output(xDIR, CW)


GPIO.setup(yDIR, GPIO.OUT)
GPIO.setup(ySTEP, GPIO.OUT)
GPIO.output(yDIR, CW)

GPIO.setup(zDIR, GPIO.OUT)
GPIO.setup(zSTEP, GPIO.OUT)
GPIO.output(zDIR, CW)

xstep_count = xSPR
delay = .0208

ystep_count = ySPR

delay = .0208

zstep_count = zSPR
delay = .0208

for x in range(xstep_count):
    GPIO.output(xSTEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(xSTEP, GPIO.LOW)
    sleep(delay)

sleep(.5)
GPIO.output(xDIR, CCW)
for x in range(xstep_count):
    GPIO.output(xSTEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(xSTEP, GPIO.LOW)
    sleep(delay)

for x in range(ystep_count):
    GPIO.output(ySTEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(ySTEP, GPIO.LOW)
    sleep(delay)

sleep(.5)

GPIO.output(yDIR, CCW)
for x in range(ystep_count):
    GPIO.output(ySTEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(ySTEP, GPIO.LOW)
    sleep(delay)

for x in range(zstep_count):
    GPIO.output(zSTEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(zSTEP, GPIO.LOW)
    sleep(delay)

sleep(.5)
GPIO.output(zDIR, CCW)
for x in range(zstep_count):
    GPIO.output(zSTEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(zSTEP, GPIO.LOW)
    sleep(delay)

GPIO.cleanup()


