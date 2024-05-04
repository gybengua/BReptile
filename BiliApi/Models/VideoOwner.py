class VideoOwner:
    def __init__(self, owner_dict): # "owner"
        self.mid:  int = owner_dict["mid"]  # user id
        self.name: str = owner_dict["name"]
        self.face: str = owner_dict["face"] # up主头像链接， sample：https://i1.hdslb.com/bfs/face/790b95c5be9be1658b4c62a3e1922c0aec694e51.jpg