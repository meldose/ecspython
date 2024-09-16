from raylib import Color, RED

class BoundingBoxInfo:
    def __init__(self, visibility=True, box_color=RED):
        self.is_visible = visibility
        self.color = box_color

