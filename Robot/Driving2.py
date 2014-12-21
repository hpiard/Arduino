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


def drive_forward(on_off):
    pin8 = board.digital[8]
    pin8.write(on_off)
    pin7 = board.digital[7]
    pin7.write(on_off)


def drive_backwards(on_off):
    pin4 = board.digital[4]
    pin4.write(on_off)
    pin12 = board.digital[12]
    pin12.write(on_off)


def left_forward(on_off):
    pin8 = board.digital[8]
    pin8.write(on_off)


def left_backwards(on_off):
    pin4 = board.digital[4]
    pin4.write(on_off)


def right_forward(on_off):
    pin7 = board.digital[7]
    pin7.write(on_off)


def right_backwards(on_off):
    pin12 = board.digital[12]
    pin12.write(on_off)


def stop_car(on_off=0):
    pin8 = board.digital[8]
    pin8.write(on_off)
    pin4 = board.digital[4]
    pin4.write(on_off)
    pin12 = board.digital[12]
    pin12.write(on_off)
    pin7 = board.digital[7]
    pin7.write(on_off)


def front_distance():
    #it = util.Iterator(board)
    #it.start()
    board.analog[ANALOG_0].enable_reporting()
    analog_value = board.analog[ANALOG_0].read()
    if analog_value == None or analog_value == 0 or analog_value == 0.0:
        analog_value = 1
    x = (3027.4 / (analog_value*1024))
    distance_front = pow(x, 1.244)
    #print (str(distance_front))
    return distance_front

'''
def rear_distance():
    it = util.Iterator(board)
    it.start()
    board.analog[ANALOG_1].enable_reporting()
    analog_value = board.analog[ANALOG_1].read()
    if analog_value == None or analog_value == 0 or analog_value == 0.0:
        analog_value = 1
    y = (3027.4 / (analog_value*1024))
    distance_rear = pow(y, 1.244)
    #print (str(distance_rear))
    return distance_rear
'''


def driving():
    while True:
        space_front = front_distance()
        print(space_front)
        #space_rear = rear_distance()
        if space_front >= 10.0:
            drive_forward(1)
        else:
            drive_forward(0)
        sleep(1)

if __main__ == '__main__':
    while True:
        it = util.Iterator(board)
        it.start()
        driving()