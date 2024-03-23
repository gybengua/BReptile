from typing import List
from BiliApi.Models.Dimension import Dimension

class VideoPage:
    def __init__(self, page_dict):
        self.Cid:        int       = page_dict["cid"]
        self.Page:       int       = page_dict["page"]
        self.From:       str       = page_dict["from"]
        self.Part:       str       = page_dict["part"]
        self.Duration:   int       = page_dict["duration"]
        self.Vid:        str       = page_dict["vid"]
        self.Weblink:    str       = page_dict["weblink"]
        self.Dimension:  Dimension = Dimension(page_dict["dimension"])
        self.FirstFrame: str       = page_dict.get("first_frame", None)

    @classmethod
    def VideoPageList(cls, page_dict_list: List[dict]):
        if page_dict_list == None:
            return None
        res = []
        for page_dict in page_dict_list:
            res.append(VideoPage(page_dict))
        return res