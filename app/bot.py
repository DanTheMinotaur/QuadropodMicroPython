from app import utils


class Motor(utils.Utils):
    def __init__(self, index):
        self._index = index
        self._current_pos = None

    async def move(self, pos):
        await self.move_servo(self._index, 500, degrees=pos)
        self.SERVOS.release(self._index)
        self._current_pos = pos

    def __str__(self):
        return f"Index: {self._index}; Position: {self._current_pos};"


class Leg:
    def __init__(self, upper, middle, lower):
        self._upper = Motor(upper)
        self._middle = Motor(middle)
        self._lower = Motor(lower)
