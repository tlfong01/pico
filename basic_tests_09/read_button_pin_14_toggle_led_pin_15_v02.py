# read_button_oin_14_toggle_led_pin_15_02

# Notes
# 1. The program loops and prints every second, therefore reponse is slow.  Need to
#    press button and hold a lillt while, say 0.5 second.

from machine import Pin
import time

led    = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

print('Press and hold 0.5 second Button pin 14 to toggle LED pin 15, <Ctrl F2> to exit program.\n')

for secondCount in range(1000):
    print('Second count =', secondCount, end = '')
    if button.value() == False:
        print('  Button not pressed, ...')
    else:
        led.toggle()
        print('  Button     pressed, LED toggled, ...')
    time.sleep(1)





