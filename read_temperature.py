__author__ = 'hpiard'
from pyfirmata import Arduino, util
import pyfirmata
from time import sleep
import os

#initialize board
port = '/dev/ttyACM0'
board = pyfirmata.Arduino(port)
#define analog ports
ANALOG_0 = 0
ANALOG_1 = 1
ANALOG_2 = 2
ANALOG_3 = 3
ANALOG_4 = 4
ANALOG_5 = 5

def calculate_celsius():
    it = util.Iterator(board)
    it.start()
    while True:
        board.analog[ANALOG_0].enable_reporting()
        analog_value = board.analog[ANALOG_0].read()
        if analog_value == None:
            analog_value = 0
        else:
            print 'Reading is: ' + str(analog_value) + ' | ',
            celsius = (analog_value - 0.5) * 100 + 4.7   # 4.7 is just a guess since I don't have the 4.7k Ohm resistor
            fahrenheit = celsius * (9.0/5.0) + 32.0
            #return celsius
            print 'Temperature in Celsius: ' + str(celsius) + ' | ',
            print 'Temperature in Fahrenheit ' + str(fahrenheit)
            sleep(3)

calculate_celsius()
