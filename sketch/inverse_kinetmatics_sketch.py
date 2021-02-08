
MAX_ANGLE = 90
MIN_ANGLE = -90

class Segment:
    def __init__(self, length: float, angle: float, resting_angle: float):
        self.length = length
        self.angle = angle
        self.resting_angle = resting_angle
        if angle is None: self.resting_angle = angle