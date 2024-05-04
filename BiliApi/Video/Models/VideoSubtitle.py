from typing import List

class SubtitleAuthor:
    def __init__(self, author_dict):
        self.mid:  int = author_dict["mid"]
        self.name: str = author_dict["name"]
        self.sex:  str = author_dict["sex"]
        self.face: str = author_dict["face"]
        self.sign: str = author_dict["sign"]
class Subtitle:
    def __init__(self, subtitle_dict):
        self.id:           int            = subtitle_dict["id"]
        self.lan:          str            = subtitle_dict["lan"]
        self.lan_doc:      str            = subtitle_dict["lan_doc"]
        self.is_lock:      str            = subtitle_dict["is_lock"]
        self.author_mid:   int            = subtitle_dict["author_mid"]
        self.subtitle_url: str            = subtitle_dict["subtitle_url"]
        self.author:       SubtitleAuthor = SubtitleAuthor(subtitle_dict["author"])

    @classmethod
    def SubtitleList(cls, subtitle_dict_list):
        if subtitle_dict_list == None:
            return []
        res = []
        for subtitle_dict in subtitle_dict_list:
            res.append(Subtitle(subtitle_dict))
        return res

class VideoSubtitle:
    def __init__(self, subtitle_dict): # "subtitle"
        self.allow_submit: bool           = subtitle_dict["allow_dict"]
        self.list:         List[Subtitle] = Subtitle.SubtitleList(subtitle_dict["list"])
