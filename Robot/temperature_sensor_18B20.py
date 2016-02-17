import pyfirmata
from pyfirmata import util
import time

port = '/dev/tty.usbmodem1411'
board = pyfirmata.Arduino(port, baudrate=57600)
print(".......connecting to Board.... stay tuned....")
print("Board connected: ", str(board.get_firmata_version()))

ANALOG_0 = 0
ANALOG_1 = 1
ANALOG_2 = 2
DIGITAL_10 = 10
DIGITAL_9 = 9
production = "yes"

# initialize the pin
DIGITAL_10 = board.get_pin("d:10:i")
# board.digital[DIGITAL_10].enable_reporting()
# board.analog[ANALOG_0].enable_reporting()
# trigger = board.digital[9]

# start iterator as recommended per Pyfirmata recommendation
it = util.Iterator(board)
it.start()


# This function measures a distance based on the HC-SR04 sensor
def measure():
    # readdate = board.digital[DIGITAL_10].read()
    readdata = DIGITAL_10
    time.sleep(2)
    return readdata


if __name__ == "__main__":
    while True:
        tempdata = measure()
        temperature = tempdata / 1000
        print("Current temperature is :", str(temperature))
        time.sleep(1)
