class Dimension:
    def __init__(self, dimension_dict): # "dimension"
        self.width:  int = dimension_dict["width"]
        self.height: int = dimension_dict["height"]
        self.rotate: int = dimension_dict["rotate"]