__author__ = 'hpiard'
__main__ = '__main__'

import pyfirmata
from pyfirmata import util
import time
from time import sleep


port = '/dev/tty.usbmodem1461'
board = pyfirmata.Arduino(port, baudrate=57600)
print(' .......connecting to Board.... stay tuned....')
print('Board connected: %s' % str(board.get_firmata_version()))

ANALOG_0 = 0
ANALOG_1 = 1
ANALOG_2 = 2
DIGITAL_6 = 6
DIGITAL_11 = 9
production = 'yes'

board.get_pin('d:6:i')
board.digital[6].enable_reporting()
trigger = board.digital[9]

# start iterator as recommended per Pyfirmata recommendation
it = util.Iterator(board)
it.start()


# This function measures a distance based on the HC-SR04 sensor
def measure():
    while True:

        echo_value = board.digital[6].read()

        trigger.write(0)

        time.sleep(0.3)

        trigger.write(1)
        time.sleep(0.00001)
        trigger.write(0)

        while echo_value == 0:
            start = time.time()

        while echo_value == 1:
            stop = time.time()

        elapsed = stop - start
        distance = elapsed / 0.000058
        print(distance)
        return distance


if __main__ == '__main__':
    while True:
        measure()
        time.time(10)