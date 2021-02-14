# Tom's Hardware Show
#  https://www.tomshardware.com/how-to/dc-motors-raspberry-pi-pico

#import temp01
import utime
from machine import Pin

motor1a = Pin(10, Pin.OUT)
motor1b = Pin(11, Pin.OUT)

def forward():
   motor1a.high()
   motor1b.low()

def backward():
   motor1a.low()
   motor1b.high()

def stop():
   motor1a.low()
   motor1b.low()

def test():
    print('  Begin test()')
    forward()
    utime.sleep(1)
    backward()
    utime.sleep(1)
    stop()
    print('  End   test()')

for i in range(1):
    print('Test ', i)
    test()

# *** End of program ***
