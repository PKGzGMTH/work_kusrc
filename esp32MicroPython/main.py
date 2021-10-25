# run code use this command $: ampy --port COM3 run .\main.py
from machine import Pin
import time
print('start!')

dataOut = Pin(23, Pin.OUT)
dataIn = Pin(22, Pin.IN)
dataOut.value(1)

while True:
    if dataIn.value() == 1:
        print('Read Succesful!')
        time.sleep_ms(400)
        break
    else:
        continue

