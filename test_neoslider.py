# /// script
# requires-python = ">=3.9"
# dependencies = ["adafruit-circuitpython-seesaw", "adafruit-blinka"]
# ///
"""Test du NeoSlider - Animation arc-en-ciel sur les LEDs."""

import time
from rainbowio import colorwheel

try:
    import board
    from adafruit_seesaw.seesaw import Seesaw
    from adafruit_seesaw import neopixel

    i2c = board.I2C()
    neoslider = Seesaw(i2c, 0x30)
    pixels = neopixel.NeoPixel(neoslider, 14, 4, pixel_order=neopixel.GRB)

except Exception:
    class FakePixels:
        def __init__(self, n):
            self.n = n

        def fill(self, color):
            print("LEDs:", [color] * self.n)

    pixels = FakePixels(4)

# Position dans la roue des couleurs
color_pos = 0

while True:
    pixels.fill(colorwheel(color_pos))
    color_pos = (color_pos + 1) % 256
    time.sleep(0.02)
