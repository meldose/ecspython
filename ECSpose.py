import numpy as np
from dataclasses import dataclass

@dataclass
class Vector3:
    x: float
    y: float
    z: float

@dataclass
class Quaternion:
    w: float
    x: float
    y: float
    z: float

class Pose:
    def __init__(self, position: Vector3 = Vector3(0, 0, 0), orientation: Quaternion = Quaternion(1, 0, 0, 0)):
        self.position = position
        self.orientation = orientation

    def __str__(self):
        return f"Position: ({self.position.x}, {self.position.y}, {self.position.z}), " \
               f"Orientation: ({self.orientation.w}, {self.orientation.x}, {self.orientation.y}, {self.orientation.z})"

    def __repr__(self):
        return self.__str__()

