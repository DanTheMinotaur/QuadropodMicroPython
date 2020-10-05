from machine import I2C, Pin
# import pca9685
import uasyncio
import utils


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



