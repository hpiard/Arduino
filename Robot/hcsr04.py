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
DIGITAL_10 = 10
DIGITAL_11 = 11
production = 'yes'

# start iterator as recommended per Pyfirmata recommendation
it = util.Iterator(board)
it.start()


# This function measures a distance based on the HC-SR04 sensor
def measure():
    time.sleep(0.5)
    echo = board.digital
    echo.read()
    trigger = board.digital[11]
    trigger.write(0)
    print('Echo Pin: %s' % echo)
    print('Trigger Pin: %s' % trigger)

    while echo == 0:
        nosig = time.time()
        print('Start time: %s' % nosig)

    trigger.write(1)
    time.sleep(0.0001)
    trigger.write(0)
    while echo == 1:
        sig = time.time()
        print('Stop time: %s' % sig)

    elapsed = sig - nosig
    distance = elapsed / 0.000058
    print(distance)
    return distance


if __main__ == '__main__':
    while True:
        x = measure()
        print('Measured distance: %s' % x)
        sleep(3)