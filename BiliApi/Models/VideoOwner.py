class VideoOwner:
    def __init__(self, owner_dict):
        self.Mid:  int = owner_dict["mid"]
        self.Name: str = owner_dict["name"] # up主名字
        self.Face: str = owner_dict["face"] # up主头像