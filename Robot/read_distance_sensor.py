__author__ = 'hpiard'
__main__ = "__main__"

#   This is a comment
from pyfirmata import Arduino, util
import pyfirmata
from time import sleep

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
        if analog_value == None:
            analog_value = 0
        else:
            print 'Front distance is: ' + str(analog_value) + ' | ',
            sleep(1)


def rear_distance():
    it = util.Iterator(board)
    it.start()
    while True:
        board.analog[ANALOG_1].enable_reporting()
        analog_value = board.analog[ANALOG_1].read()
        if analog_value == None:
            analog_value = 0
        else:
            print 'Rear distance is: ' + str(analog_value)
            sleep(1)

if __main__ == "__main__":
    front_distance()
    rear_distance()