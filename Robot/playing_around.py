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

echo = board.get_pin('d:6:i')
trigger = board.get_pin('d:9:o')

it = util.Iterator(board)
it.start()


echo.enable_reporting()

trigger.write(0)
time.sleep(0.5)
trigger.write(1)
time.sleep(0.01)
trigger.write(0)
start = time.time()
print(start)
while echo.read() == 0:
    nosig = time.time()
    print(nosig)

while echo.read() == 1:
    sig = time.time()
    print(sig)

elapsed = sig - nosig
distance = elapsed * 0.000058

print(distance)