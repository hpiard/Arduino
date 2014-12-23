__author__ = 'hpiard'
__main__ = '__main__'

import pyfirmata
from pyfirmata import util
from time import sleep
from threading import Thread

ANALOG_0 = 0
ANALOG_1 = 1
#distance_front = 1
#distance_rear = 1
#on_off = 0

port = '/dev/tty.usbmodem1461'
board = pyfirmata.Arduino(port, baudrate=57600)



def distance_hcsr04():
    while True:
            board.analog[ANALOG_2].enable_reporting()
            analog_value = board.analog[ANALOG_2].read()
            # print "\n"
            # print "Actual reading: " + str(analog_value)
            if analog_value == None or analog_value == 0 or analog_value == 0.0:
                analog_value = 1
            # print "Calculated Reading: " + str(analog_value * 1024)
            x = (3027.4 / (analog_value*1024))
            global distance_front
            distance_front = pow(x, 1.2134)
            # return pow(x, 1.2134)
            # print "============================================"
            # print "Front distance is: " + str(analog_value)
            # print "Calculated Front Distance:" + str(distance) + " cm"
            # print "============================================"
            print (str(distance_front))
            sleep(1)

