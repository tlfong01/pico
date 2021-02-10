# toggle_led_01.py tlfog01 2021feb10hkt2032
# Description - Toggle LED each executi8on of program

# References - Getting started with Raspberry Pi Pico Projects - tlfog01  2021feb10hkt2032
# https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/2

# Setup - To upgrade Thonny
# sudo apt update && sudo apt upgrade -y

# *** print_hello_world_01.py ***

from machine import Pin

print('Begin toggleLed()')
print('  ...')

led = Pin(25, Pin.OUT) # On board LED = pin 15
led.toggle()

print('End   toggle LED')

# .END

# *** Sample Output - tlfong01  2021feb10hkt2043 ***

'''
>>> %Run -c $EDITOR_CONTENT
Begin toggleLed()
  ...
End   toggle LED
>>> 
'''
# *** End of sample output ***
