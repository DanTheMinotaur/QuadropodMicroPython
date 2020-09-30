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
    u = utils.Utils()

    u.test_servo_motor(0, 90)
    u.test_servo_motor(0, 160)
    u.test_servo_motor(0, 10)
    # u.test_servo_motor(0, 90)
    # u.test_servo_motor(0, 90)
    # await u.move_servo(5, 1000, degrees=10)
    # await u.move_servo(5, 1000, degrees=50)
    # await u.move_servo(5, 1000, degrees=90)
    # await u.move_servo(5, 1000, degrees=130)
    # await u.move_servo(5, 1000, degrees=170)
    # await u.move_servo(5, 1000, degrees=90)

    # while True:
    #     u.INTERNAL_LED.value(True)
    #     await uasyncio.sleep_ms(500)
    #     u.INTERNAL_LED.value(False)
    #     await uasyncio.sleep_ms(700)

    # leg = Leg(upper=0, middle=1, lower=2)
    # while True:
    #     await leg.up()
    #     await uasyncio.sleep_ms(1000)
    #     await leg.down()
    #     await uasyncio.sleep_ms(1000)
    # for i in range(16):
    #     await uasyncio.create_task(move(i, Leg.SERVO_MIN, 0))
    #
    # await uasyncio.sleep_ms(1000)
    #
    # for i in range(16):
    #     await uasyncio.create_task(move(i, Leg.SERVO_MAX, 0))
    #
    # await uasyncio.sleep_ms(1000)
    #
    # for i in range(16):
    #     await uasyncio.create_task(move(i, Leg.SERVO_MID, 0))
    #
    # await uasyncio.sleep_ms(1000)



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


