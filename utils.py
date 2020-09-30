import pca9685
from machine import I2C, Pin
import uasyncio
from time import sleep


class Utils:
    INTERNAL_LED = Pin(2, Pin.OUT)
    SERVOS = pca9685.Servos(I2C(scl=Pin(5), sda=Pin(4)))
    SERVO_MAX = 170
    SERVO_MID = 90
    SERVO_MIN = 10
    DEFAULT_WAIT_MS = 150

    async def move_servo(self, motor_index, period_ms=None, **kwargs):
        self.SERVOS.position(motor_index, **kwargs)
        if period_ms:
            await uasyncio.sleep_ms(period_ms)

    async def blink_internal_led(self, on_period_ms=500, off_period_ms=500):
        self.INTERNAL_LED.value(True)
        await uasyncio.sleep_ms(on_period_ms)
        self.INTERNAL_LED.value(False)
        await uasyncio.sleep_ms(off_period_ms)

    def test_servo_motor(self, motor_index, degrees):
        self.SERVOS.position(motor_index, degrees=degrees)
        sleep(2)
        self.SERVOS.release(motor_index)
        self.INTERNAL_LED.value(True)
