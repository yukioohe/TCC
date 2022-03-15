import RPi.GPIO as GPIO
import time as delay

FQ_UD = 35
W_CLK = 36
DATA = 37
RESET = 38

CLOCK = 125000000

def pulse(pin):
    GPIO.output(pin, GPIO.HIGH)
    GPIO.output(pin, GPIO.LOW)
    

def down():
    GPIO.output(FQ_UD, GPIO.LOW)
    GPIO.output(W_CLK, GPIO.LOW)
    GPIO.output(DATA, GPIO.LOW)
    GPIO.output(RESET, GPIO.LOW)

def AD9850_init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(FQ_UD, GPIO.OUT)
    GPIO.setup(W_CLK, GPIO.OUT)
    GPIO.setup(DATA, GPIO.OUT)
    GPIO.setup(RESET, GPIO.OUT)
    
    down()
    pulse(FQ_UD)
    pulse(W_CLK)
    pulse(RESET)

def calibrate(calibrate_freq):
    CLOCK = calibrate_freq

def trf_byte(data):
    for x in range(8):
        data >>= 1
        GPIO.output(DATA, data & 0x01)
        pulse(W_CLK)

def set_freq(freq):
    deltaphase = freq*4294967296/CLOCK
    deltaphase = int(deltaphase)

    for x in range(4):
        deltaphase >>= 8
        trf_byte(freq & 0xFF)
    trf_byte(0x000)
    pulse(FQ_UD)        


AD9850_init()
calibrate(124999500)


try:
    while True:
        set_freq(1000)
except KeyboardInterrupt:
   GPIO.cleanup()




