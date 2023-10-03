import RPi.GPIO as GPIO
from config.cfg.DIR import *
import sys
from threading import Thread
GPIO.setmode(GPIO.BCM)


class Motor:
    def __init__(self, EnA, EnB, In1, In2, In3, In4, speed=0):
        self.EnLeft = EnA
        self.EnRight = EnB
        self.InLeft1 = In1
        self.InLeft2 = In2
        self.InRight1 = In3
        self.InRight2 = In4
        GPIO.setup(self.EnLeft, GPIO.OUT)
        GPIO.setup(self.EnRight, GPIO.OUT)
        GPIO.setup(self.InLeft1, GPIO.OUT)
        GPIO.setup(self.InLeft2, GPIO.OUT)
        GPIO.setup(self.InRight1, GPIO.OUT)
        GPIO.setup(self.InRight2, GPIO.OUT)
        
        self.pwmLeft = GPIO.PWM(self.EnLeft, 100)
        self.pwmLeft.start(0)
        self.pwmRight = GPIO.PWM(self.EnRight, 100)
        self.pwmRight.start(0)

        self.speed = speed

        self.direction = {
            FORWARD:  [GPIO.HIGH, GPIO.LOW,  GPIO.HIGH, GPIO.LOW ],
            BACKWARD: [GPIO.LOW,  GPIO.HIGH, GPIO.LOW,  GPIO.HIGH],
            LEFT:     [GPIO.LOW,  GPIO.HIGH, GPIO.HIGH, GPIO.LOW ],
            RIGHT:    [GPIO.HIGH, GPIO.LOW,  GPIO.LOW,  GPIO.HIGH],
            STOP:     [GPIO.LOW,  GPIO.LOW,  GPIO.LOW,  GPIO.LOW ]
        }

        self.isRunning = False
        self.start = Thread(target=self.go)


    def move(self, direction=FORWARD, speed=None, timeout=0):
        if speed is not None:
            self.speed = speed
        self.change_dir(direction)


    def change_dir(self, direction):
        direction = self.direction.get(direction)
        if direction is None:
            print('[ERROR] Unknown direction is given!')
            sys.exit(1)
        self.isRunning = False if direction == STOP else True
        # left side
        GPIO.output(self.InLeft1, direction[0])
        GPIO.output(self.InLeft2, direction[1])
        # right side
        GPIO.output(self.InRight1, direction[2])
        GPIO.output(self.InRight2, direction[3])


    def go(self):
        while self.isRunning:
            self.pwmLeft.ChangeDutyCycle(abs(self.speed))
            self.pwmRight.ChangeDutyCycle(abs(self.speed))
