import numpy as np
import RPi.GPIO as GPIO
import datetime
import time
WL=[-2.25410598e-03,  1.11667167e+00,  2.31076908e+01]
WR=[-1.86278271e-03,  8.45057718e-01,  5.70439913e+01]
TRIG=29
ECHO=31
VL=12
VR=36
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(VL,GPIO.OUT)
GPIO.setup(VR,GPIO.OUT)

VL1=GPIO.PWM(VL,50)
VR1=GPIO.PWM(VR,50)
VL1.start(0)
VR1.start(0)
def ultrasonic():
	GPIO.output(TRIG,False)
	time.sleep(0.0002)
	GPIO.output(TRIG,True)
	time.sleep(0.00001)
	GPIO.output(TRIG,False)
	while GPIO.input(ECHO)==0:
		pulse_start=time.time()
	while GPIO.input(ECHO)==1:
		pulse_end=time.time()
	pulse_duration=pulse_end-pulse_start
	distance=pulse_duration*17150
	distance=int(round(distance,2))
	if distance>400:

		distance=400
	return distance
i=1    
while i==1:
        s=ultrasonic()
        s = [s**2,s,1]
        s = np.array(s)
        print(s)        
        Yx = s.dot(WL)
        Yy=s.dot(WR)
        if(Yx>20):
                Y1=Yx
        else:
                Y1=20
        if(Yy>20):
                Y2=Yy
        else:
                Y2=20
        if(Yx>100):
                Y1=100
        else:
                Y1=Yx
        if(Yy>100):
                Y2=100
        else:
                Y2=Yy        

        VL1.ChangeDutyCycle(Y1)
        VR1.ChangeDutyCycle(Y2)


