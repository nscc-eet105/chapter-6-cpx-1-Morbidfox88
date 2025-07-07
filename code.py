from adafruit_circuitplayground import cp
import time# Write your code here :-)

def on():
    for i in range(10):
        cp.pixels[i] = (0, 100, 0)

def off():
    for i in range(10):
        cp.pixels[i] = (0, 0, 0)

while True:
    if cp.touch_A1:
        on()
    else:
        off()











