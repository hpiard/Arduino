__author__ = 'hpiard'
__init__ = '__init__'

import pyfirmata
from pyfirmata import util
from time import sleep


port = '/dev/ttyACM0'
board = pyfirmata.Arduino(port)


def left_forward(on_off):
    it = util.Iterator(board)
    it.start()
    pin0 = board.get_pin('d:3:o')
    pin0.write(on_off)


if __init__ == '__init__':
    left_forward(1)
    sleep(2)
    left_forward(1)