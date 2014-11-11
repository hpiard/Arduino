__author__ = 'hpiard'
__main__ = "__main__"

#   This is a comment
from pyfirmata import Arduino, util
import pyfirmata
from time import sleep
import math

#initialize board
port = '/dev/ttyACM1'
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
        print "\n"
        print "Actual reading: " + str(analog_value)
        if analog_value == None or analog_value == 0 or analog_value == 0.0:
            analog_value = 1
        #print "Calculated Reading: " + str(analog_value * 1024)
        x = (3027.4 / (analog_value*1024))
        distance = pow(x, 1.2134)
        print "============================================"
        #print "Front distance is: " + str(analog_value)
        print "Calculated Front Distance:" + str(distance) + " cm"
        print "============================================"
        sleep(2)


def rear_distance():
    it = util.Iterator(board)
    it.start()
    while True:
        board.analog[ANALOG_1].enable_reporting()
        analog_value = board.analog[ANALOG_1].read()
        print "\n"
        print "Actual reading: " + str(analog_value)
        if analog_value == None or analog_value == 0 or analog_value == 0.0:
            analog_value = 1
        #print "Calculated Reading: " + str(analog_value * 1024)
        y = (3027.4 / (analog_value*1024))
        distance = pow(y, 1.2134)
        print "============================================"
        #print "Rear distance is: " + str(analog_value)
        print "Calculated Rear Distance:" + str(distance) + " cm"
        print "============================================"
        sleep(2)

if __main__ == "__main__":
    front_distance()
    rear_distance()