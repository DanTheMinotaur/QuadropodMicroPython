from app.bot import Leg
import uasyncio

legs = {
    "left_front": Leg(0, 1, 2),
    "left_back": Leg(3, 4, 5),
    "right_front": Leg(9, 10, 11),
    "right_back": Leg(6, 7, 8)
}


"""
Test for leg class to use through REPL

from uasyncio import run
from tests.leg import move_leg, default, flat, sit, stand, legs, walk_forward

"""


def move_leg(leg, upper, middle, lower):
    _map = {
        'lf': "left_front",
        'rb': "right_back",
        'rf': "right_front",
        'lb': "left_back"
    }
    uasyncio.run(legs[_map[leg]].move_to(upper, middle, lower))


def default():
    async def set_defaults():
        pos = [
            legs["left_front"].move_to(90, 120, 30),
            legs["left_back"].move_to(90, 60, 150),
            legs["right_front"].move_to(90, 60, 150),
            legs["right_back"].move_to(35, 120, 30)
        ]
        await uasyncio.gather(*pos)
    uasyncio.run(set_defaults())


def flat():
    async def set_flat():
        await uasyncio.gather(
            legs["right_front"].move_to(upper_pos=90, middle_pos=30, lower_pos=30),
            legs["left_back"].move_to(upper_pos=90, middle_pos=30, lower_pos=30),
            legs["right_back"].move_to(upper_pos=90, middle_pos=150, lower_pos=150),
            legs["left_front"].move_to(upper_pos=90, middle_pos=150, lower_pos=150)
        )

    uasyncio.run(set_flat())


def sit():
    async def set_sit():
        await uasyncio.gather(
            legs["left_front"].move_to(None, 90, 30),
            legs["left_back"].move_to(None, 90, 150),
            legs["right_front"].move_to(None, 90, 150),
            legs["right_back"].move_to(None, 90, 30)
        )

    uasyncio.run(set_sit())


def stand():
    async def set_stand():
        await uasyncio.gather(
            legs["left_front"].move_to(None, 90, 10),
            legs["left_back"].move_to(None, 90, 170),
            legs["right_front"].move_to(None, 90, 170),
            legs["right_back"].move_to(None, 90, 10)
        )
        await uasyncio.gather(
            legs["left_front"].move_to(None, 150, 20),
            legs["left_back"].move_to(None, 30, 160),
            legs["right_front"].move_to(None, 30, 160),
            legs["right_back"].move_to(None, 150, 20)
        )
        await uasyncio.gather(
            legs["left_front"].move_to(None, 120, 30),
            legs["left_back"].move_to(None, 60, 150),
            legs["right_front"].move_to(None, 60, 150),
            legs["right_back"].move_to(None, 120, 30)
        )
    uasyncio.run(set_stand())


def stand2():
    async def set_stand():
        await uasyncio.gather(
            legs["left_front"].move_to(None, 90, 10),
            legs["left_back"].move_to(None, 90, 170),
            legs["right_front"].move_to(None, 90, 170),
            legs["right_back"].move_to(None, 90, 10)
        )
        await uasyncio.gather(
            legs["left_front"].move_to(None, 150, 20),
            legs["left_back"].move_to(None, 30, 160),
            legs["right_front"].move_to(None, 30, 160),
            legs["right_back"].move_to(None, 150, 20)
        )
    uasyncio.run(set_stand())


def walk_forward():
    async def inner():
        await legs["left_front"].move_to(30, 80, None)
        await legs["left_front"].move_to(None, 120, None)

    uasyncio.run(inner())
