import time
from machine import Pin, ADC


def measure_water_level(water_level_switch, adc):
    water_level_switch.value(1)
    time.sleep(1)
    value = adc.read_u16()
    time.sleep(1)
    water_level_switch.value(0)
    return value

led = Pin(25, Pin.OUT)
lamp = Pin(22, Pin.OUT)
pump = Pin(20, Pin.OUT)
water_level_switch = Pin(16, Pin.OUT)


adc = ADC(26)
led.value(1)
time.sleep(2)

led.value(0)
time.sleep(2)

water_level_switch.value(0)
lamp.value(0)
pump.value(0)
pump.value(1)
time.sleep(5)
pump.value(0)
while True:
    led.toggle()
    time.sleep(1)

   

