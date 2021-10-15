# run code use this command $: ampy --port COM3 run .\main.py
from machine import Pin
import time
print('start!')

led = Pin(23, Pin.OUT)

for i in range(100): 
    led.value(1)
    time.sleep_ms(50)
    led.value(0)
    time.sleep_ms(50)

