__author__ = 'hpiard'

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
    def __init__(self, front_sensor, back_sensor):
        self.front_sensor = left_sensor
        self.back_sensor = back_sensor


car = Driving("lfw", "lbw", "rfw", "rbw")

car.output_in_text()