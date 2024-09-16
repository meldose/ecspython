import random
from raylib import Vector3

class EcsPickPattern:
    def __init__(self):
        scale = 3.0
        self.points = []
        for _ in range(100):
            p = Vector3(
                random.uniform(-scale, scale),
                random.uniform(-scale, scale),
                random.uniform(-scale, scale)
            )
            self.points.append(p)

