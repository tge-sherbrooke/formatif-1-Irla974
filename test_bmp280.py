# /// script
# requires-python = ">=3.9"
# dependencies = [
# "adafruit-circuitpython-bmp280",
# "adafruit-blinka",
# "rpi-gpio"
# ]
# ///
"""
Test du capteur BMP280 via STEMMA QT / I2C
Compatible Raspberry Pi OS récent + uv
"""

import time
import board
import adafruit_bmp280

Init I2C
i2c = board.I2C()

Adresse courante : 0x77 (change à 0x76 si besoin)
sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x77)

sensor.sea_level_pressure = 1013.25

while True:
    print(f"Température : {sensor.temperature:.1f} °C")
    print(f"Pression    : {sensor.pressure:.1f} hPa")
    print(f"Altitude    : {sensor.altitude:.1f} m")
    print("-" * 30)

    time.sleep(1)
