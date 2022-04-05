#!/usr/bin/python
# -*- coding:utf-8 -*-


from platform import freedesktop_os_release
import time
import ADS1256
import AD9850
import RPi.GPIO as GPIO
import plot


BOARD_FQ_UD = 35
BOARD_W_CLK = 36
BOARD_D7_SERIAL = 37
BOARD_RESET = 38
frequency = 10000

try:
    ADC = ADS1256.ADS1256()
    ADC.ADS1256_init()

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(BOARD_FQ_UD, GPIO.OUT)
    GPIO.setup(BOARD_W_CLK, GPIO.OUT)
    GPIO.setup(BOARD_D7_SERIAL, GPIO.OUT)
    GPIO.setup(BOARD_RESET, GPIO.OUT)
    DDS = AD9850.ad9850(BOARD_FQ_UD, BOARD_W_CLK, BOARD_D7_SERIAL, BOARD_RESET, 125000000)
    DDS.initialize()

    

    while(1):
        
        DDS.set_freq(frequency)
        ADC_Value = ADC.ADS1256_GetChannalValue(0)
        value = ADC_Value*5.0/0x7fffff
        print ("0 ADC = %lf"%(value))
        plot.plot(value)
        
except :
    GPIO.cleanup()
    print ("\r\nProgram end     ")
    exit()







