from adafruit_circuitplayground import cp
import time# Write your code here :-)

while True:
    for i in range(10):
        cp.pixels[i] = (0, 100, 0)
        time.sleep(.5)


    cp.pixels.fill((0, 0, 0))
    time.sleep(1.0)


    for i in range(9, -1, -1):
        cp.pixels[i] = (255, 0, 0)
        time.sleep(0.5)

    cp.pixels.fill((0, 0, 0))
    time.sleep(1.0)


