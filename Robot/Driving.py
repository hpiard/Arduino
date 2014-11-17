__author__ = 'hpiard'
__main__ = "__main__"
import pyfirmata
from read_distance_sensor import rear_distance
from read_distance_sensor import front_distance

"""
Analog Port 0 = Front Sensor --> front_sensor
Analog Port 2 = Rear Sensor --> rear_sensor
"""
#initialize arduino board
#initialize board
port = '/dev/ttyACM0'
board = pyfirmata.Arduino(port)

class Drive(object):
    def __init__(self, left_forward, left_backwards, right_forward, right_backwards, stop):
        self.left_forward = left_forward
        self.left_backwards = left_backwards
        self.right_forward = right_forward
        self.right_backwards = right_backwards
        self.stop = stop


    def left_forward(self, on_off=0):
        digital_pin0 = board.get_pin('d:0:o')
        digital_pin0.write(on_off)

    def left_backwards(self, on_off=0):
        digital_pin1 = board.get_pin('d:1:o')
        digital_pin1.write(on_off)

    def right_forward(self, on_off=0):
        digital_pin3 = board.get_pin('d:3:o')
        digital_pin3.write(on_off)

    def right_backwards(self, on_off=0):
        digital_pin2 = board.get_pin('d:2:o')
        digital_pin2.write(on_off)

    def stop(self, on_off=0):
        digital_pin0 = board.get_pin('d:0:o')
        digital_pin0.write(on_off)
        digital_pin1 = board.get_pin('d:1:o')
        digital_pin1.write(on_off)
        digital_pin2 = board.get_pin('d:2:o')
        digital_pin2.write(on_off)
        digital_pin3 = board.get_pin('d:3:o')
        digital_pin3.write(on_off)

'''
class Sensors(object):
    def __init__(self, front_sensor, rear_sensor):
        self.front_sensor = front_sensor
        self.rear_sensor = rear_sensor

    def read_sensors(self):
        print "xxx"
'''
#car = Driving("lfw", "lbw", "rfw", "rbw")
#car.output_in_text()
# Define Port where board is attached to
#PORT = '/dev/ttyACM1'
# Creates a new board
#board = pyfirmata.Arduino(PORT)
#Firmata_version = get_firmata_version()
#print(board)

if __main__ == "__main__":
    #front_distance()
    #rear_distance()
    left_forward(1)