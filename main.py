#!/usr/bin/python
# -*- coding:utf-8 -*-


import time
import ADS1256
import AD9850
import RPi.GPIO as GPIO
import plot


try:
    ADC = ADS1256.ADS1256()
    ADC.ADS1256_init()
    plot.plot()
        
except :
    GPIO.cleanup()
    print ("\r\nProgram end     ")
    exit()







