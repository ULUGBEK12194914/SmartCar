from config import cfg
from config.cfg.DIR import *
from RPi import GPIO
from motor import Motor
GPIO.setwarnings(False)

motor = Motor(EnA=cfg.MOTOR.ENA,
              EnB=cfg.MOTOR.ENB,
              In1=cfg.MOTOR.IN1,
              In2=cfg.MOTOR.IN2,
              In3=cfg.MOTOR.IN3,
              In4=cfg.MOTOR.IN4)

print("'w' forward\n's' - backward\n'a' - left\n'd' - right")

direction = {
    'w': FORWARD,
    's': BACKWARD,
    'a': LEFT,
    'd': RIGHT
}

while True:
    d = input('>>> ')
    d = direction.get(d)
    d = STOP if d is None else d
    motor.move(d, 50)
    if d == 'q': break
