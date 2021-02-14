# blink_led_pin_15_01.py tlfog01 2021feb10hkt2032
# Description - bBlink LED Pin15

# References - Getting started with Raspberry Pi Pico Projects - tlfog01  2021feb10hkt2032
# https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/2

# Setup - To upgrade Thonny
# sudo apt update && sudo apt upgrade -y

# *** blink_led_pin_15.py ***

from machine import Pin, Timer

# *** Config ***

led15   = Pin(15, Pin.OUT)
timer15 = Timer()

#*** Functions ***

def blinkLed15(timer):
    led15.toggle()
    return

def main01(frequency):
    print('Begin blinkLedPin15()')    
    timer15.init(freq = frequency, mode = Timer.PERIODIC, callback = blinkLed15)     
    print('End   blinkLedPin15()')
    return 

# *** Main() ***

frequency = 3
main01(frequency) 

# .END

# *** Sample Output - tlfong01  2021feb10hkt2043 ***

'''
>>> %Run -c $EDITOR_CONTENT
Begin blinkLedPin15()
End   blinkLedPin15()
>>> 
'''
# *** End of sample output ***



