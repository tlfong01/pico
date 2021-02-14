# pwm_fade_in_out_led_pin_15_02, tlfong01  2021feb12hkt1542

from machine import Pin, PWM
from time import sleep

# Config
pwm = PWM(Pin(15))
pwm.freq(1000)

# *** Functions ***

def pwmFadeInOutLed(pwmPin, counTotal):
    print('Begin pwmFadeInOutLed() \n')
    
    print('  PWM fade in fade out LED pin ', pwmPin, ' ', countal, 'times')  
    for count in range(countTotal):
        print('count =', count)
        for duty in range(65025):
            pwm.duty_u16(duty)
            sleep(0.0001)
        for duty in range(65025, 0, -1):
            pwm.duty_u16(duty)
            sleep(0.0001)
            

    
        
