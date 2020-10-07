from app.bot import Motor


async def move(index, position):
    motor = Motor(index)
    await motor.move(position)
    print(motor)