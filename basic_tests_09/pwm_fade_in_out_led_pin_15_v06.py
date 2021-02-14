# pwm_fade_in_out_led_pin_15_06, tlfong01  2021feb12hkt1542

# References
#   https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/7

from machine import Pin, PWM
from time    import sleep

# *** Config ***

# nil

# *** Functions ***

def pwmFadeInOutLed(pwmPinNum, pwmFreq,  countTotal):

    pwmPin = PWM(Pin(pwmPinNum))
    pwmPin.freq(pwmFreq)  
    
    print('  PWM fade in fade out LED pin', pwmPinNum, countTotal, 'times')
        
    for count in range(countTotal):
        print('    count =', count)
        for duty in range(65025):
            pwmPin.duty_u16(duty)
            sleep(0.0001)
        for duty in range(65025, 0, -1):
            pwmPin.duty_u16(duty)
            sleep(0.0001)
    return            
          
def main01(): 
    print('Begin pwmFadeInOutLed() \n')
    
    pwmPinNum  = 15
    pwmFreq    = 1000
    countTotal = 4    
    
    pwmFadeInOutLed(pwmPinNum, pwmFreq,  countTotal)         
    
    print('\nEnd   pwmFadeInOutLed() \n')
    
    return

# *** Main ***

main01()

# *** End ***

# *** Sample Output  tlfong01  2021feb12hkt1619 ***

'''
>>> %Run -c $EDITOR_CONTENT
Begin pwmFadeInOutLed() 

  PWM fade in fade out LED pin 15 4 times
    count = 0
    count = 1
    count = 2
    count = 3

End   pwmFadeInOutLed() 

>>>
'''

# *** End of Samploe Output


    
    
    
    
          

    
        



