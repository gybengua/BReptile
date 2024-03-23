from typing import List

class SubtitleAuthor:
    def __init__(self, author_dict):
        self.Mid:  int = author_dict["mid"]
        self.Name: str = author_dict["name"]
        self.Sex:  str = author_dict["sex"]
        self.Face: str = author_dict["face"]
        self.Sign: str = author_dict["sign"]

class Subtitle:
    def __init__(self, subtitle_dict):
        self.Id:          int            = subtitle_dict["id"]
        self.Lan:         str            = subtitle_dict["lan"]
        self.LanDoc:      str            = subtitle_dict["lan_doc"]
        self.IsLock:      bool           = subtitle_dict["is_lock"]
        self.AuthorMid:   int            = subtitle_dict["author_mid"]
        self.SubtitleUrl: str            = subtitle_dict["subtitle_url"]
        self.Author:      SubtitleAuthor = SubtitleAuthor(subtitle_dict["author"])

    @classmethod
    def SubtitleList(self, subtitle_dict_list):
        if subtitle_dict_list == None:
            return None

        res = []
        for subtitle_dict in subtitle_dict_list:
            res.append(Subtitle(subtitle_dict))
        return res

class VideoSubtitle:
    def __init__(self, subtitle_dict):
        self.AllowSubmit: bool           = subtitle_dict["allow_submit"]
        self._List:       List[Subtitle] = Subtitle.SubtitleList(subtitle_dict["list"])

