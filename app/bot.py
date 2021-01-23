from app import utils
import uasyncio


class Motor(utils.Utils):
    def __init__(self, index):
        self._index = index
        self._current_pos = None

    async def move(self, pos=None):
        if pos is None:
            pos = self._current_pos
        await self.move_servo(self._index, 500, degrees=pos)
        self.SERVOS.release(self._index)
        self._current_pos = pos

    def __str__(self):
        return "Index: {}; Position: {};".format(
            self._index,
            self._current_pos
        )


class Leg:
    def __init__(self, upper, middle, lower, leg_pos=''):
        self._upper = Motor(upper)
        self._middle = Motor(middle)
        self._lower = Motor(lower)
        self._leg_pos = leg_pos

    async def move_to(self, upper_pos=None, middle_pos=None, lower_pos=None):
        await uasyncio.gather(
            self._upper.move(upper_pos),
            self._middle.move(middle_pos),
            self._lower.move(lower_pos)
        )

    def __str__(self):
        return 'Position: {};\nUpper: {};\nMiddle: {};\nLower: {};'.format(
            self._leg_pos,
            self._upper,
            self._middle,
            self._lower
        )