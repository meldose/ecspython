import raylibpy as ry

class EcsModelComponent:
    def __init__(self, model_file=None, texture_file=None):
        if model_file and texture_file:
            self.model = ry.load_model(model_file)
            self.texture = ry.load_texture(texture_file)
            self.model.materials[0].maps[ry.MATERIAL_MAP_DIFFUSE].texture = self.texture
        elif model_file:
            self.model = ry.load_model(model_file)
        else:
            self.model = None
            self.texture = None

    def __copy__(self):
        return EcsModelComponent(self.model, self.texture)

