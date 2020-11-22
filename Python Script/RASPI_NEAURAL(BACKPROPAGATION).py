import numpy as np
import RPi.GPIO as GPIO
import datetime
import time
WR1=[[ -5.92562853 , -7.94746133],
 [ 41.67166532 , -2.60726736],
 [-88.65573554 , -0.5908581 ],
 [-75.25103451 ,  7.14947258]]
WR2=[[ -2.26808846  ,-1.80482169 ,-16.79030316,  -1.32299546]]

WL1=[[ -5.44913178 , -3.29779068],
 [ -7.07241217 , -3.08602923],
 [-13.5659067  , -0.32136291],
 [  5.66266272 , -1.26304783]]
WL2=[[-3.00249839, -3.60115211 ,-6.03566308 ,-2.82482123]]
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
def sigmoid (x):
    y = 1/(1 + np.exp(-x))
    return y
   
def sigmoid_derivative(x):
    return x * (1 - x)
i=1    
while i==1:
    Ai=ultrasonic()
    Ai = [Ai/1000,1]
    Ai = np.array(Ai)
    hiddeni1 = sigmoid(np.dot(WL1, Ai)).reshape(-1, 1)
    YL = sigmoid(np.dot(WL2, hiddeni1)).reshape(-1,1)
    hiddeni2 = sigmoid(np.dot(WR1, Ai)).reshape(-1, 1)
    YR = sigmoid(np.dot(WR2, hiddeni2)).reshape(-1,1)
    YL=YL*1000
    YR=YR*1000
    if(YL>20):
        Y1=YL
    else:
        Y1=20
        
    if(YR>100):
        Y1=100
    else:
        Y1=YR
               

    VL1.ChangeDutyCycle(Y1)
    VR1.ChangeDutyCycle(Y2)


