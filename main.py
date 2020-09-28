from machine import I2C, Pin
import pca9685
import uasyncio

INTERNAL_LED = Pin(2, Pin.OUT)

"""
servos = servo.Servos(I2C(scl=Pin(5), sda=Pin(4))
for i in range(16):
    servos.position(i, us=1500)
"""

servos = pca9685.Servos(I2C(scl=Pin(5), sda=Pin(4)))


async def move(servo_pos, degrees, period_ms):
    servos.position(servo_pos, degrees=degrees)
    await uasyncio.sleep_ms(period_ms)


class Leg:
    SERVO_MAX = 170
    SERVO_MIN = 10
    DEFAULT_WAIT_MS = 150

    def __init__(self, upper, middle, lower):
        self._upper = upper
        self._middle = middle
        self._lower = lower

    async def up(self):
        await uasyncio.create_task(move(self._middle, self.SERVO_MAX, self.DEFAULT_WAIT_MS))

    async def down(self):
        await uasyncio.create_task(move(self._middle, self.SERVO_MIN, self.DEFAULT_WAIT_MS))


async def main():
    leg = Leg(upper=0, middle=1, lower=2)
    while True:
        await leg.up()
        await uasyncio.sleep_ms(1000)
        await leg.down()
        await uasyncio.sleep_ms(1000)


uasyncio.run(main())

# async def blink(led):
#     while True:
#         led.value(True)
#         await uasyncio.sleep_ms(500)
#         led.value(False)
#         await uasyncio.sleep_ms(700)
#
#
# async def main():
#     await uasyncio.create_task(blink(INTERNAL_LED))
#
# uasyncio.run(main())
# pos = 10
# while True:
#     pos += 30
#     if pos >= 170:
#         pos = 10
#     servos.position(0, degrees=pos)
#     # for i in range(16):
#     #     servos.position(i, us=1500)
#     time.sleep(1.5)
#     INTERNAL_LED.value(True)
#     time.sleep(0.1)
#     INTERNAL_LED.value(False)


