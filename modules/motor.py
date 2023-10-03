import RPi.GPIO as GPIO
from threading import Thread
GPIO.setmode(GPIO.BCM)


class Motor():
    def __init__(self, EnA, EnB, In1, In2, In3, In4):
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
        
        self.speed_left = 0
        self.speed_right = 0
        self.isRunning = False
        self.start = Thread(target=self.go)
    
    def move(self, direction, speed=0):
        if not self.isRunning:
            # start driving
            self.isRunning = True
            self.start.start()
        
        if speed > 100.0: speed = 100.0
        elif speed < 0.0: speed = 0.0
        if direction == 'f':        # forward
            self.speed_left = self.speed_right = speed
            self.wheel('f')
        elif direction == 'b':      # backward
            self.speed_left = self.speed_right = -speed
            self.wheel('b')
        elif direction == 'r':      # right
            if self.speed_left > 50.0: self.speed_left = 50.0
            self.speed_left = self.speed_left + speed if (self.speed_left+speed) < 100.0 else 100
            self.speed_right = self.speed_left - speed if (self.speed_left-speed) >= 0.0 else 0.0
        elif direction == 'l':      # left
            if self.speed_right > 50.0: self.speed_right = 50.0
            self.speed_right = self.speed_right + speed if (self.speed_right+speed) < 100.0 else 100
            self.speed_left = self.speed_right - speed if (self.speed_right-speed) >= 0.0 else 0.0
        else:
            self.speed_left = self.speed_right = 0.0
            if direction == 'q':
                # stop driving
                self.isRunning = False
                self.start.join()
                
    def go(self):
        while self.isRunning:
            self.pwmLeft.ChangeDutyCycle(abs(self.speed_left))
            self.pwmRight.ChangeDutyCycle(abs(self.speed_right))
        
    def wheel(self, direction):
        if direction == 'f':        # forward
            # left side
            GPIO.output(self.InLeft1, GPIO.HIGH)
            GPIO.output(self.InLeft2, GPIO.LOW)
            # right side
            GPIO.output(self.InRight1, GPIO.HIGH)
            GPIO.output(self.InRight2, GPIO.LOW)
        elif direction == 'b':      # backward
            # left side
            GPIO.output(self.InLeft1, GPIO.LOW)
            GPIO.output(self.InLeft2, GPIO.HIGH)
            # right side
            GPIO.output(self.InRight1, GPIO.LOW)
            GPIO.output(self.InRight2, GPIO.HIGH)

