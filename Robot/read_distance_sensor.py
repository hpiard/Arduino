__author__ = 'hpiard'
__main__ = "__main__"

'''
You must run Python 3.4.2
This web site helped me with the formula for sensor "Sharp 2YOA21":
http://www.basicxandrobotics.com/additions/new%20sharp/index.html
'''

#   This is a comment
from time import sleep
from threading import Thread

from pyfirmata import util
import pyfirmata


#initialize board
port = '/dev/tty.usbmodem1461'
board = pyfirmata.Arduino(port)
print('....warming up your Arduino Board..... stay tuned....')
print('This Board runs Firmware: %s' % str(board.get_firmata_version()))

# start iterator as recommended per Pyfirmata recommendation
it = util.Iterator(board)
it.start()

# define analog ports
ANALOG_0 = 0
ANALOG_1 = 1
distance_front = 1
distance_rear = 1


def front_distance():
    while True:
        board.analog[ANALOG_0].enable_reporting()
        analog_value = board.analog[ANALOG_0].read()
        # print "\n"
        # print "Actual reading: " + str(analog_value)
        if analog_value == None or analog_value == 0 or analog_value == 0.0:
            analog_value = 1
        # print "Calculated Reading: " + str(analog_value * 1024)
        x = (3027.4 / (analog_value*1024))
        global distance_front
        distance_front = pow(x, 1.2134)
        # return pow(x, 1.2134)
        # print "============================================"
        # print "Front distance is: " + str(analog_value)
        # print "Calculated Front Distance:" + str(distance) + " cm"
        # print "============================================"
        print (str(distance_front))
        sleep(1)


def rear_distance():
    while True:
        board.analog[ANALOG_1].enable_reporting()
        analog_value = board.analog[ANALOG_1].read()
        # print "\n"
        # print "Actual reading: " + str(analog_value)
        if analog_value == None or analog_value == 0 or analog_value == 0.0:
            analog_value = 1
        # print "Calculated Reading: " + str(analog_value * 1024)
        y = (3027.4 / (analog_value*1024))
        global distance_rear
        distance_rear = pow(y, 1.2134)
        # return pow(y, 1.2134)
        # print "============================================"
        # print "Rear distance is: " + str(analog_value)
        # print "Calculated Rear Distance:" + str(distance) + " cm"
        # print "============================================"
        print (str(distance_rear))
        sleep(1)

if __main__ == "__main__":
    Thread(target=front_distance).start()
    Thread(target=rear_distance).start()

