from machine import I2C, Pin
import time
import pca9685

"""
servos = servo.Servos(I2C(scl=Pin(5), sda=Pin(4))
for i in range(16):
    servos.position(i, us=1500)
"""

servos = pca9685.Servos(I2C(scl=Pin(5), sda=Pin(4)))
led = Pin(2, Pin.OUT)
while True:
    for i in range(16):
        servos.position(i, us=1500)
    time.sleep(3)
    time.sleep(0.1)
    led.value(True)
    time.sleep(0.1)
    led.value(False)


