import math
from raylib import Vector3, Color

class EcsPathComponent:
    def __init__(self):
        lastX = 0.0
        lastY = 0.0
        scaling = 1.0
        step_size = 0.002
        steps = 5000
        c_scale = 255.0 / steps
        self.points = []
        self.phi = []
        self.colors = []

        for i in range(steps):
            s = i * step_size
            scale = scaling * (0.5 + 0.25 * math.sin(85.0 * s))

            p = Vector3()
            c = Color()
            
            p.x = scale * (5.0 * (math.sin(20.0 * s) + 0.1 * math.sin(20.0 * s)) * 20.0 / (s + 20))
            p.y = scale * (5.0 * (-math.cos(20.0 * s) - 0.1 * math.cos(20.0 * s)) * 20.0 / (s + 20))
            p.z = 10.0 * s / 20.0
            
            c.a = 255
            c.r = int(i * c_scale)
            c.g = int(255 - i * c_scale)
            c.b = 0
            
            self.points.append(p)
            self.phi.append(math.atan2(p.y - lastY, p.x - lastX))
            self.colors.append(c)

            lastX = p.x
            lastY = p.y
        
        self.phi[0] = self.phi[1]

