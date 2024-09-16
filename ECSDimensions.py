from dataclasses import dataclass

@dataclass
class Vector3:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

class Dimensions:
    def __init__(self, min_corner: Vector3 = Vector3(), max_corner: Vector3 = Vector3()):
        self.min = min_corner
        self.max = max_corner

