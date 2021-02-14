# read_button_oin_14_toggle_led_pin_15_01


from machine import Pin
import time

led    = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

#while True:
#    print('Press Button Now, ...')
#    if button.value():
#        print('Button pin 14 pressed, will toggle LED pin 15, ...')
#     led.toggle()
#     time.sleep(1)

print('Press and hold 0.5 second Button pin 14 to toggle LED pin 15, <Ctrl F2> to exit program.\n')

for secondCount in range(1000):
    print('Second count =', secondCount, end = '')
    if button.value() == False:
        print('  Button not pressed, ...')
    else:
        print('  Button     pressed, will toggle LED, ...')
    time.sleep(1)




