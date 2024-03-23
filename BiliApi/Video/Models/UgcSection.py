from typing import List
from BiliApi.Video.Models.UgcEpisode import UgcEpisode

class UgcSection:
    def __init__(self, section_dict):
        self.SeasonId: int = section_dict["season_id"]
        self.Id:       int = section_dict["id"]
        self.Title:    str = section_dict["title"]
        self.Type:     int = section_dict["type"]
        self.Episodes: List[UgcEpisode] = UgcEpisode.UgcEpisodeList(section_dict["episodes"])

    @classmethod
    def UgcSectionList(cls, section_dict_list):
        if section_dict_list == None:
            return None

        res = []
        for section_dict in section_dict_list:
            res.append(UgcSection(section_dict))
        return res