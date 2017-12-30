#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import sys

move="Move not specified"
T=1
P=0.7

LeftGo=37
RightGo=33
LeftBack=31
RightBack=35
PINS=[LeftGo,LeftBack,RightGo,RightBack]

F=(LeftGo,RightGo)
B=(LeftBack,RightBack)
L=(LeftBack,RightGo)
R=(LeftGo,RightBack)



def setup():
    GPIO.setmode(GPIO.BOARD)    
    for i in PINS:
        GPIO.setup(i, GPIO.OUT)  
        GPIO.output(i, GPIO.LOW) 

def Move(port,duration,percent,T1=0.001):
    t=0
    t1=T1
    t0=(1-percent)*t1/percent
    while t<duration:
        GPIO.output(port, GPIO.HIGH)  # led on
        time.sleep(t1)
        GPIO.output(port, GPIO.LOW)  # led on
        time.sleep(t0)
        t=t+t1+t0

def Go(duration, percent=0.7):
    Move(F,duration,percent)
def Back(duration,percent=0.7):
    Move(B,duration,percent)

def Left(duration,percent=0.7):
    Move(L,duration,percent)
def Right(duration,percent=0.7):
    Move(R,duration,percent)

def loop():
    Go(2,0.5)
    Left(2,0.2)
    Go(1,0.5)
    Right(2,0.2)
    Go(1,0.5)
    Back(2,0.5)
    destroy()

def destroy():
    for i in PINS:
	GPIO.output(i, GPIO.LOW)  
    GPIO.cleanup()               
 


if __name__ == '__main__':     
    if len(sys.argv)<>4:
        print 'invalid args'
    else:
        move=sys.argv[1]
        T=float(sys.argv[2])
        P=float(sys.argv[3])

        vs=['L','R','F','B']
        if move in vs:
            try:
                destroy()
            except:
                pass
            setup()
            if move=="L":
                Left(T,P)
            elif move=="R":
                Right(T,P)
            elif move=="F":
                Go(T,P)
            elif move=="B":
                Back(T,P)
            destroy()


