from typing import List
from BiliApi.Models.Dimension import Dimension

class VideoPage:
    def __init__(self, page_dict):
        self.cid:         int       = page_dict["cid"]
        self.dimension:   Dimension = Dimension(page_dict["dimension"])
        self.duration:    int       = page_dict["duration"]
        self.first_frame: str       = page_dict["first_frame"]
        self._from:       str       = page_dict["from"]
        self.page:        int       = page_dict["page"]
        self.part:        str       = page_dict["part"]
        self.vid:         str       = page_dict["vid"]
        self.weblink:     str       = page_dict["weblink"]

    @classmethod
    def VideoPageList(cls, page_dict_list: List[dict]): # "pages
        if page_dict_list == None:
            return []
        res = []
        for page_dict in page_dict_list:
            res.append(VideoPage(page_dict))
        return res
