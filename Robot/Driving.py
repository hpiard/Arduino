__author__ = 'hpiard'
__main__ = "__main__"
import pyfirmata
from read_distance_sensor import rear_distance
from read_distance_sensor import front_distance

"""
Analog Port 0 = Front Sensor --> front_sensor
Analog Port 2 = Rear Sensor --> rear_sensor
"""
class Driving(object):
    def __init__(self, left_forward, left_backward, right_forward, right_backward):
        self.left_forward = left_forward
        self.left_backward = left_backward
        self.right_forward = right_forward
        self.right_backward = right_backward

    def output_in_text(self):
        print "I am a class and I can drive: %s %s %s %s" % (self.left_forward, self.left_backward,
                                                             self.right_forward, self.right_backward)

class Sensors(object):
    def __init__(self, front_sensor, rear_sensor):
        self.front_sensor = front_sensor
        self.rear_sensor = rear_sensor

    def read_sensors(self):
        print "xxx"

#car = Driving("lfw", "lbw", "rfw", "rbw")
#car.output_in_text()
# Define Port where board is attached to
#PORT = '/dev/ttyACM1'
# Creates a new board
#board = pyfirmata.Arduino(PORT)
#Firmata_version = get_firmata_version()
#print(board)

if __main__ == "__main__":
    front_distance()
    rear_distance()