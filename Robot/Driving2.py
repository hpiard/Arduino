__author__ = 'hpiard'
__init__ = '__init__'

import pyfirmata
from pyfirmata import util
from time import sleep


ANALOG_0 = 0
ANALOG_1 = 1

port = '/dev/ttyACM0'
board = pyfirmata.Arduino(port)


def left_forward(on_off=0):
    #it = util.Iterator(board)
    #it.start()
    pin9 = board.digital[9]
    pin9.write(on_off)


def left_backwards(on_off=0):
    #it = util.Iterator(board)
    #it.start()
    pin6 = board.digital[6]
    pin6.write(on_off)


def right_forward(on_off=0):
    #it = util.Iterator(board)
    #it.start()
    pin3 = board.digital[3]
    pin3.write(on_off)


def right_backwards(on_off=0):
    #it = util.Iterator(board)
    #it.start()
    pin5 = board.digital[5]
    pin5.write(on_off)


def stop_car(on_off=0):
    #it = util.Iterator(board)
    #it.start()
    pin9 = board.digital[9]
    pin9.write(on_off)
    pin6 = board.digital[6]
    pin6.write(on_off)
    pin5 = board.digital[5]
    pin5.write(on_off)
    pin3 = board.digital[3]
    pin3.write(on_off)


def front_distance():
    it = util.Iterator(board)
    it.start()
    board.analog[ANALOG_0].enable_reporting()
    analog_value = board.analog[ANALOG_0].read()
    #print "\n"
    #print "Actual reading: " + str(analog_value)
    if analog_value == None or analog_value == 0 or analog_value == 0.0:
        analog_value = 1
        #print "Calculated Reading: " + str(analog_value * 1024)
        x = (3027.4 / (analog_value*1024))
        distance = pow(x, 1.2134)
        #return pow(x, 1.2134)
        #print "============================================"
        #print "Front distance is: " + str(analog_value)
        #print "Calculated Front Distance:" + str(distance) + " cm"
        #print "============================================"
        #print str(distance)
        return distance


def rear_distance():
    it = util.Iterator(board)
    it.start()
    board.analog[ANALOG_1].enable_reporting()
    analog_value = board.analog[ANALOG_1].read()
    #print "\n"
    #print "Actual reading: " + str(analog_value)
    if analog_value == None or analog_value == 0 or analog_value == 0.0:
        analog_value = 1
        #print "Calculated Reading: " + str(analog_value * 1024)
        y = (3027.4 / (analog_value*1024))
        distance = pow(y, 1.2134)
        #return pow(y, 1.2134)
        #print "============================================"
        #print "Rear distance is: " + str(analog_value)
        #print "Calculated Rear Distance:" + str(distance) + " cm"
        #print "============================================"
        #print str(distance)
        return distance


def driving():
    while True:
        front = front_distance()
        back = rear_distance()
        if front >= 3.7259080757:
            left_forward(1)
            right_forward(1)
        else:
            stop_car()
            print front
            print back
            sleep(1)


if __init__ == '__init__':
    driving()