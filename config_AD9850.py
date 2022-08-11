import AD9850
import RPi.GPIO as GPIO

BOARD_FQ_UD = 19
BOARD_W_CLK = 16
BOARD_D7_SERIAL = 26
BOARD_RESET = 20
DDS = AD9850.ad9850(BOARD_FQ_UD, BOARD_W_CLK, BOARD_D7_SERIAL, BOARD_RESET, 125000000)

def init_AD9850(freq):

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BOARD_FQ_UD, GPIO.OUT)
    GPIO.setup(BOARD_W_CLK, GPIO.OUT)
    GPIO.setup(BOARD_D7_SERIAL, GPIO.OUT)
    GPIO.setup(BOARD_RESET, GPIO.OUT)
    
    
    global DDS
    DDS.initialize()
    DDS.set_freq(freq)
    
    
def set_freq(frequency):
    global DDS
    DDS.set_freq(int(frequency))