from app.bot import Leg
import uasyncio

left_front = Leg(0, 1, 2)
left_back = Leg(3, 4, 5)
right_front = Leg(9, 10, 11)
right_back = Leg(6, 7, 8)

"""
Test for leg class to use through REPL

import uasyncio
from tests.leg import set_defaults, set_flat, set_stand

uasyncio.run()
"""


async def set_defaults():
    pos = [
        left_front.move_to(upper_pos=90, middle_pos=150, lower_pos=30),
        right_back.move_to(upper_pos=90, middle_pos=150, lower_pos=30),
        right_front.move_to(upper_pos=90, middle_pos=30, lower_pos=150),
        left_back.move_to(upper_pos=90, middle_pos=30, lower_pos=150)
    ]
    await uasyncio.gather(*pos)


async def set_flat():
    await uasyncio.gather(
        right_front.move_to(upper_pos=90, middle_pos=30, lower_pos=30),
        left_back.move_to(upper_pos=90, middle_pos=30, lower_pos=30),
        right_back.move_to(upper_pos=90, middle_pos=150, lower_pos=150),
        left_front.move_to(upper_pos=90, middle_pos=150, lower_pos=150)
    )


async def sit():
    await uasyncio.gather(
        left_front.move_to(upper_pos=90, middle_pos=180, lower_pos=30),
        right_front.move_to(90, 110, 80)
    )


# async def move_leg():
#     left_front = Leg(0, 1, 2)
#     left_back = Leg(3, 4, 5)
#
#     await left_front.move_to(upper_pos=90, middle_pos=150, lower_pos=30)  # Default position
#
#     await left_front.move_to(upper_pos=150, middle_pos=90, lower_pos=90)
#
#     await left_front.move_to(upper_pos=90, middle_pos=150, lower_pos=30)
#
#     await left_front.move_to(upper_pos=30, middle_pos=90, lower_pos=150)
#     # await left_back.move_to()

