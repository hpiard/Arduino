from nanpy import ArduinoApi
from nanpy import SerialManager
from time import sleep
from time import time

connection = SerialManager()
a = ArduinoApi(connection=connection)

trig = 13
echo = 12
ledrouge = 11
ledbleu = 10

a.pinMode(trig, a.OUTPUT)
a.pinMode(echo, a.INPUT)
a.pinMode(ledrouge, a.OUTPUT)
a.pinMode(ledbleu, a.OUTPUT)

a.digitalWrite(trig, a.LOW)
sleep(0.5)
a.digitalWrite(trig, a.HIGH)
sleep(0.00001)
a.digitalWrite(trig, a.LOW)
start = time()

while a.digitalRead(echo) == 0:
        start = time()

while a.digitalRead(echo) == 1:
        stop = time()

elapsed = stop - start

distance = elapsed * 34000
distance = distance / 2

# print "Distance : %.lf" % distance

if distance < 4:
        a.digitalWrite(ledrouge, a.HIGH)
        a.digitalWrite(ledbleu, a.LOW)
else:
        a.digitalWrite(ledrouge, a.LOW)
        a.digitalWrite(ledbleu, a.HIGH)

if distance >= 200 or distance <= 0:
        print "Out of Range"
else:
        print "Distance : %.lf cm" % distance

sleep(0.05)