import RPi.GPIO as GPIO
from time import time, sleep
GPIO.setmode(GPIO.BCM)


class Ultrasonic:
	def __init__(self, trig, echo, unit='m'):
		self.unit = unit
		self.setup(trig, echo)
	
	def setup(self, trig, echo):
		self.trig = trig
		self.echo = echo
		GPIO.setup(self.trig, GPIO.OUT)
		GPIO.setup(self.echo, GPIO.IN)
		GPIO.output(self.trig, False)
	
	def get_distance(self, timeout=0.1, unit=None):
		if unit is None:
			unit = self.unit
		GPIO.output(self.trig, True)
		sleep(0.00001)
		GPIO.output(self.trig, False)
		while GPIO.input(self.echo) == 0:
			pulse_start = time()
		while GPIO.input(self.echo) == 1:
			pulse_end = time()
		pulse_duration = pulse_end - pulse_start
		distance = round(pulse_duration * 171.50, 5)
		sleep(timeout)
		if unit == 'cm':
			distance *= 100
		return distance


class Tracer:
    """
    InfraRed Tracers are digital out
    - either they detect black surface and output low (0V)
    - or they do not detect black surface and output high (5V)
    """
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.IN)
    
    def isBlack(self, timeout=0.1):
        sleep(timeout)
        if GPIO.input(self.pin) == 0:
            return False
        return True


class ObjectAvoidance:
    """
    InfraRed Object Avoidance sensors are digital out
    - either they detect an object and output low (0V)
    - or they do not detect any and output high (5V)
    """
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.IN)
    
    def isObjectExist(self, timeout=0.1):
        sleep(timeout)
        if GPIO.input(self.pin) == 0:
            return True
        return False
