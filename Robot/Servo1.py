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


def drive_forward   (on_off):
    pin8 = board.digital[8]
    pin8.write(on_off)
    pin7 = board.digital[7]
    pin7.write(on_off)

'''
def drive_forward2(on_off):
    pin8 = board.get_pin('d:8:p')
    pin8.write(on_off)
    pin7 = board.get_pin('d:7:p')
    pin7.write(on_off)
'''


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


def move():
    while True:
        drive_forward(1)
        print('driving forward')
        sleep(3)
        drive_forward(0)
        print('stopped')
        sleep(1)


if __main__ == '__main__':
    move()