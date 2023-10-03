from easydict import EasyDict as edict

__C                     = edict()

# config can be used by: from config import cfg
cfg                     = __C


# Ultrasonic distance sensor's options
__C.ULTRA               = edict()
__C.ULTRA.TRIG          = 24
__C.ULTRA.ECHO          = 25


# Motors' options
__C.MOTOR               = edict()
__C.MOTOR.IN1           = 4
__C.MOTOR.IN2           = 17
__C.MOTOR.IN3           = 27
__C.MOTOR.IN4           = 22
__C.MOTOR.ENA           = 18
__C.MOTOR.ENB           = 23

# car's movement directions
__C.DIR                 = edict()
__C.DIR.FORWARD         = 0
__C.DIR.BACKWAR         = 1
__C.DIR.LEFT            = 2
__C.DIR.RIGHT           = 3
__C.DIR.STOP            = 4

# InfraRed sensors' option
__C.IR                  = edict()

# OA - Object Avoidance
__C.IR.OA               = edict()
__C.IR.OA.RIGHT         = 26 
__C.IR.OA.LEFT          = 13

# Tracer Sensors
__C.IR.TRACER           = edict()
__C.IR.TRACER.RIGHT     = 6
__C.IR.TRACER.LEFT      = 5
