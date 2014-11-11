__author__ = 'hpiard'
__main__ = "__main__"

#   This is a comment
from pyfirmata import Arduino, util
import pyfirmata
from time import sleep
import math

#initialize board
port = '/dev/ttyACM0'
board = pyfirmata.Arduino(port)
#define analog ports
ANALOG_0 = 0
ANALOG_1 = 1


def front_distance():
    it = util.Iterator(board)
    it.start()
    while True:
        board.analog[ANALOG_0].enable_reporting()
        analog_value = board.analog[ANALOG_0].read()
        #if analog_value == None:
        #    analog_value = 0
        #else:
        print "\n"
        print analog_value
        if analog_value == None:
            analog_value = 1
        distance = ((67870.0 / (analog_value - 3.0)) - 40.0)
        print "============================================"
        print "Front distance is: " + str(analog_value)
        print "Calculated Distance:" + str(distance) + " cm"
        print "============================================"
        sleep(2)


def rear_distance():
    it = util.Iterator(board)
    it.start()
    while True:
        board.analog[ANALOG_1].enable_reporting()
        analog_value = board.analog[ANALOG_1].read()
        #if analog_value == None:
        #    analog_value = 0
        #else:
        print "\n"
        print analog_value
        if analog_value == None:
            analog_value = 1
        volts = analog_value * 0.0048828125
        distance = 65*pow(volts, -1.10)
        print "============================================"
        print "Rear distance is: " + str(analog_value)
        print "Calculated Distance:" + str(distance) + " cm"
        print "============================================"
        sleep(2)

if __main__ == "__main__":
    #front_distance()
    rear_distance()