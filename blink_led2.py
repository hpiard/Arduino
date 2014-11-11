__author__ = 'hpiard'
__main__ = "__main__"
import pyfirmata

# Pin definitions (digital pins
PIN13 = 13          # Pin 13 is used
PIN12 = 12          # Pin 12 is used
DELAY_1_SEC = 1     # A 1 second delay
DELAY_2_SEC = 2     # A 2 seconds delay
DELAY_3_SEC = 3     # A 3 seconds delay
DELAY_4_SEC = 4     # A 4 seconds delay
DELAY_5_SEC = 5     # A 5 seconds delay
DELAY_6_SEC = 6     # A 6 seconds delay
DELAY_7_SEC = 7     # A 7 seconds delay
DELAY_8_SEC = 8     # A 8 seconds delay
DELAY_9_SEC = 9     # A 9 seconds delay
DELAY_10_SEC = 10   # A 10 seconds delay
# Define Port where board is attached to
PORT = '/dev/ttyACM0'
# Creates a new board
board = pyfirmata.Arduino(PORT)
print(board)

# Function for green LED
def green_led():
    counter_PIN13 = 0

    while True:
        board.digital[PIN13].write(1)   # Set the LED pin to 1 (HIGH)
        board.pass_time(DELAY_1_SEC)
        read_pin13 = board.digital[PIN13].read()
        #print(read_pin13)
        board.digital[PIN13].write(0)   # Set the LED pin to 0 (LOW)
        board.pass_time(DELAY_1_SEC)
        counter_PIN13 += read_pin13
        print 'Counter of PIN 13 is at position ' + str(counter_PIN13)

        if counter_PIN13 == 3:
            red_led()
            break

# Function for red LED
def red_led():
    counter_PIN12 = 0
    while True:
        board.digital[PIN12].write(1)   # Set the LED pin to 1 (HIGH)
        board.pass_time(DELAY_1_SEC)
        read_pin12 = board.digital[PIN12].read()
        board.digital[PIN12].write(0)   # Set the LED pin to 0 (LOW)
        board.pass_time(DELAY_1_SEC)
        counter_PIN12 += read_pin12
        print 'Counter of PIN 12 is at position ' + str(counter_PIN12)
        if counter_PIN12 == 5:
            green_led()
            break

def count_loop():
    loops = 0
    loops += 1
    print 'We are in loop #' + str(loops)

if __main__ == "__main__":
    green_led()
    #lock = thread.allocate_lock()
    #thread.start_new_thread(green_led(), ("Thread #: 1", 2, lock))