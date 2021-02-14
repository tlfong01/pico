# toggle_led_pin25_01.py tlfog01 2021feb11hkt1732
# Description - Toggle system LED Pin25 when executed

# References
# 1. Getting started with Raspberry Pi Pico Projects - tlfog01  2021feb10hkt2032
# https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/2

# Notes Notes
# CLI command to upgrade Thonny
# $ sudo apt update && sudo apt upgrade -y
# $ sudo reboot now

# *** Debug print statements  ***

from machine import Pin

print('Begin toggleSystemLedPin25()')

led = Pin(25, Pin.OUT) # On board LED = pin 15
led.toggle()

print('End   toggleSystemLedPin25')

# .END

# *** Sample Output - tlfong01  2021feb10hkt2043 ***
# Notes
# System on board LED toggles on and off eveary time program exceutes
# Press <Ctrl-S> to compile, <F5> to run

'''
MicroPython v1.14 on 2021-02-02; Raspberry Pi Pico with RP2040
Type "help()" for more information.
>>> %Run -c $EDITOR_CONTENT
Begin toggleSystemLedPin25()
End   toggleSystemLedPin25
>>> %Run -c $EDITOR_CONTENT
Begin toggleSystemLedPin25()
End   toggleSystemLedPin25
'''
# *** End of sample output ***
