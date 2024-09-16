import raylibpy as rl

class EcsModelComponent:
    def __init__(self, model_file=None, texture_file=None):
        if model_file and texture_file:
            self.model = rl.load_model(model_file)
            self.texture = rl.load_texture(texture_file)
            self.model.materials[0].maps[rl.MATERIAL_MAP_DIFFUSE].texture = self.texture
        elif model_file:
            self.model = rl.load_model(model_file)
        else:
            self.model = None
            self.texture = None

    def __copy__(self):
        return EcsModelComponent(self.model, self.texture)

