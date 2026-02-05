# /// script
# requires-python = ">=3.9"
# dependencies = [
#   "adafruit-circuitpython-seesaw",
#   "adafruit-blinka",
#   "rpi-gpio"
# ]
# ///

"""
Test du NeoSlider – animation arc-en-ciel
"""

import time
import board
from rainbowio import colorwheel
from adafruit_seesaw.seesaw import Seesaw
from adafruit_seesaw import neopixel

# Init I2C
i2c = board.I2C()

# NeoSlider est à l'adresse 0x30 (PAS de keyword)
neoslider = Seesaw(i2c, 0x30)

# 4 LEDs NeoPixel sur le pin 14
pixels = neopixel.NeoPixel(
    neoslider,
    14,     # pin
    4,      # nombre de LEDs
    pixel_order=neopixel.GRB,
    auto_write=True
)

color_pos = 0

while True:
    pixels.fill(colorwheel(color_pos))
    color_pos = (color_pos + 1) % 256
    time.sleep(0.02)
