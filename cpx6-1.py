from adafruit_circuitplayground import cp
import time
import random

pattern = [0, 9, 8, 3, 5, 2, 6, 7, 1, 4]

def pixel_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)

def blackout():
    cp.pixels.fill((0, 0, 0))


while True:
    cp.pixels.fill((0, 0, 0,))
    time.sleep(1.0)
    for pixel in pattern:
        cp.pixels[pixel] = pixel_color()
        time.sleep(1.0)
        cp.pixels[pixel] = (0, 0, 0)

    time.sleep(1.0)

blackout()




