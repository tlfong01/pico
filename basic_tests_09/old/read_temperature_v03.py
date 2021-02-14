# read_temperature_v04 tlfong01  2021feb13hkt2024
# Reference:
#   RandomNerd https://RandomNerdTutorials.com

import machine, onewire, ds18x20, time

# *** Config ***

tempSensorPinNum = 27
tempSensorPin    = machine.Pin(tempSensorPinNum)
tempSensor       = ds18x20.DS18X20(onewire.OneWire(tempSensorPin))

# *** Functions ***

def main01():
    roms = tempSensor.scan()
    print('Temp Sensor DS18B20: ', roms)

    for secondCount in range(1000):
        print('Second count =', secondCount, ' ', end = '')    
        tempSensor.convert_temp()
        time.sleep_ms(750)
        for rom in roms:
            print(tempSensor.read_temp(rom))        
        time.sleep(1)
    return

# *** main() ***

main01()

# *** End ***

# *** Sample Code ***

'''

'''

# ***Ｅｎｄ　ｏｆ　ｓｍｐｌｅ　ｃｏｄｅ
