class Vector3:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

class Acceleration:
    def __init__(self, val=None):
        if val is None:
            self.value = Vector3()
        else:
            self.value = val

