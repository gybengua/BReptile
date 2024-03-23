class Dimension:
    def __init__(self, dimension_dict):
        self.Width:  int = dimension_dict["width"]
        self.Height: int = dimension_dict["height"]
        self.Rotate: int = dimension_dict["rotate"]