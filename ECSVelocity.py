import Vector3

class Velocity:
    def __init__(self, val=None):
        self.value = Vector3.Vector3() if val is None else val

