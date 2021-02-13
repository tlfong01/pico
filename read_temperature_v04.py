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

    for secondCount in range(4):
        print('Second ', secondCount, ' ', end = '')    
        tempSensor.convert_temp()
        time.sleep_ms(750)
        for rom in roms:
            print("%.2f" % tempSensor.read_temp(rom))
            time.sleep(1)
    return

# *** main() ***

main01()

# *** End of program ***

# *** Sample Output ***

'''
>>> %Run -c $EDITOR_CONTENT
Temp Sensor DS18B20:  [bytearray(b'(\x85\xd2y\xa2\x16\x03\xe4')]
Second count = 0  21.75
Second count = 1  21.75
Second count = 2  21.81
Second count = 3  21.81
>>> 

'''

# *** .End ***

