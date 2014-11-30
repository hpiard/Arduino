__author__ = 'hpiard'
__init__ = '__init__'

import pyfirmata
from pyfirmata import util
from time import sleep
from threading import Thread

ANALOG_0 = 0
ANALOG_1 = 1
distance_front = 1
distance_rear = 1
on_off = 0

port = '/dev/tty.usbmodem1421'
board = pyfirmata.Arduino(port)


def left_forward(on_off):
    pin9 = board.digital[9]
    pin9.write(on_off)


def left_backwards(on_off):
    pin6 = board.digital[6]
    pin6.write(on_off)


def right_forward(on_off):

    pin3 = board.digital[3]
    pin3.write(on_off)


def right_backwards(on_off):

    pin5 = board.digital[5]
    pin5.write(on_off)


def stop_car(on_off):
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
    if analog_value == None or analog_value == 0 or analog_value == 0.0:
        analog_value = 1
    x = (3027.4 / (analog_value*1024))
    distance_front = pow(x, 1.2134)
    print (str(distance_front))
    return distance_front


def rear_distance():
    it = util.Iterator(board)
    it.start()
    board.analog[ANALOG_1].enable_reporting()
    analog_value = board.analog[ANALOG_1].read()
    if analog_value == None or analog_value == 0 or analog_value == 0.0:
        analog_value = 1
    y = (3027.4 / (analog_value*1024))
    distance_rear = pow(y, 1.2134)
    print (str(distance_rear))
    return distance_rear



def driving():
    while True:
        space_front = front_distance()
        #space_rear = rear_distance()
        if space_front > 10.0:
            left_forward(1)
            right_forward(1)
        elif space_front < 10.0:
            left_forward(0)
            right_forward(0)
        sleep(1)

if __init__ == '__init__':
    driving()