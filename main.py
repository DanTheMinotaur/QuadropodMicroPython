from machine import I2C, Pin
# import pca9685
import uasyncio
import utils

# INTERNAL_LED = Pin(2, Pin.OUT)

"""
servos = servo.Servos(I2C(scl=Pin(5), sda=Pin(4))
for i in range(16):
    servos.position(i, us=1500)
"""

# servos = pca9685.Servos(I2C(scl=Pin(5), sda=Pin(4)))


# async def move(servo_pos, degrees, period_ms):
#     servos.position(servo_pos, degrees=degrees)
#     await uasyncio.sleep_ms(period_ms)


class Leg(utils.Utils):
    def __init__(self, upper, middle, lower):
        self._upper = upper
        self._middle = middle
        self._lower = lower

    async def up(self):
        await uasyncio.create_task(
            self.move_servo(self._middle, self.DEFAULT_WAIT_MS, degrees=self.SERVO_MAX)
        )

    async def down(self):
        await uasyncio.create_task(
            self.move_servo(self._middle, self.DEFAULT_WAIT_MS, degrees=self.SERVO_MIN)
        )


async def main():
    pass


uasyncio.run(main())



