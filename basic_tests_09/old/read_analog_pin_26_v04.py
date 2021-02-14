# read_analog_pin_16_v05.py  tlfong01  2021feb12hkt1852

from machine import Pin, PWM, ADC
import time

# *** Config and Setup ***

analogPinNum = 26
analogPin01  = ADC(Pin(analogPinNum))

# *** Functions ***

def getAdcResults(analogPin):
    adcResults = analogPin.read_u16()
    return adcResults

# *** Main Test Functions ***

def main01():
    analogPin = analogPin01
    for secondCount in range(1000):
        print('Second count =', secondCount, end = '')    
        adcResults = getAdcResults(analogPin)
        print(' ADC results =', adcResults)
        time.sleep(1)
    return

# *** Main ***

main01()

# *** End ***

'''
Sample output  tlfong01  2021feb12hkt2208
>>> %Run -c $EDITOR_CONTENT
Second count = 0 ADC results = 30103
Second count = 1 ADC results = 30151
Second count = 2 ADC results = 30183
Second count = 3 ADC results = 30119
Second count = 4 ADC results = 30119
Second count = 5 ADC results = 30183
Second count = 6 ADC results = 30055
Second count = 7 ADC results = 30183
'''

# *** End of smaple output ***