# pwm_fade_in_out_led_pin_1502

from machine import Pin, PWM
from time import sleep

pwm = PWM(Pin(15))
pwm.freq(1000)

while True:
    for duty in range(65025):
        pwm.duty_u16(duty)
        sleep(0.0001)
    for duty in range(65025, 0, -1):
        pwm.duty_u16(duty)
        sleep(0.0001)