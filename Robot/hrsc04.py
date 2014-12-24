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
TRIGGER = board.digital[11]
stop = 0
start = 0

# start iterator as recommended per Pyfirmata recommendation
it = util.Iterator(board)
it.start()


# This function measures a distance based on the HC-SR04 sensor
def measure():
    sleep(2)

    board.analog[ANALOG_2].enable_reporting()
    echo = board.analog[ANALOG_2].read()
    global start
    global stop
    TRIGGER.write(0)
    while echo == 0:
        start = time.time()
        print('Start time: %s' % start)

    while echo == 1:
        stop = time.time()
        print('Stop time: %s' % stop)

    elapsed = stop - start
    distance = elapsed / 0.000058

    return distance

print(measure())
quit()

'''
if __main__ == '__main__':
    while True:
        x = measure()
        print('Measured distance: %s' % x)
        sleep(3)
'''