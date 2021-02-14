# read_analog_pin_16_v01.py  tlfong01  2021feb12hkt1852

from machine import Pin, PWM, ADC

# *** Config and Setup ***

pwmPinNum    = 15
analogPinNum = 26
pwmFreq      = 1000

pwmPin01 = PWM(Pin(pwmPinNum))
pwmPin01.freq(pwmFreq)

analogPin01 = ADC(Pin(analogPinNum))

# *** Functions ***

def getAdcResults(analogPin):
    adcResults = analogPin.read_u16()
    return adcResults

# *** Main Test Functions ***

def main01():
    analogPin = analogPin01
    adcResults = getAdcResults(analogPin)
    print('ADC results =', adcResults)
    
# *** Main ***

main01()

# *** End ***




