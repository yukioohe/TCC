#!/usr/bin/python
# -*- coding:utf-8 -*-


import time
import ADS1256
import AD9850
import RPi.GPIO as GPIO
import plot


BOARD_FQ_UD = 19
BOARD_W_CLK = 16
BOARD_D7_SERIAL = 26
BOARD_RESET = 20
frequency = 10000



try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BOARD_FQ_UD, GPIO.OUT)
    GPIO.setup(BOARD_W_CLK, GPIO.OUT)
    GPIO.setup(BOARD_D7_SERIAL, GPIO.OUT)
    GPIO.setup(BOARD_RESET, GPIO.OUT)
    DDS = AD9850.ad9850(BOARD_FQ_UD, BOARD_W_CLK, BOARD_D7_SERIAL, BOARD_RESET, 125000000)
    DDS.initialize()
    
    ADC = ADS1256.ADS1256()
    ADC.ADS1256_init()
    DDS.set_freq(frequency)
    plot.plot(value)
        
except :
    GPIO.cleanup()
    print ("\r\nProgram end     ")
    exit()







