from typing import List
from BiliApi.Video.Models.UgcEpisode import UgcEpisode

class UgcSection:
    def __init__(self, section_dict):
        self.episodes:  List[UgcEpisode] = UgcEpisode.UgcEpisodeList(section_dict["episodes"])
        self.id:        int              = section_dict["id"]
        self.season_id: int              = section_dict["season_id"]
        self.title:     str              = section_dict["title"]
        self.type:      int              = section_dict["type"]

        @classmethod
        def UgcSectionList(cls, section_dict_list):
            if section_dict_list == None:
                return []
            res = []
            for section_dict in section_dict_list:
                res.append(UgcSection(section_dict))
            return res