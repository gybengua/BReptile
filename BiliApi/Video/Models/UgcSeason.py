from typing import List
from BiliApi.Video.Models.UgcSection import UgcSection
from BiliApi.Video.Models.UgcStat    import UgcStat

class UgcSeason:
    def __init__(self, ugc_season_dict):
        if(ugc_season_dict == None):
            return None

        self.id:         int = ugc_season_dict["id"]
        self.Title:      str = ugc_season_dict["title"] # 合集名称
        self.Cover:      str = ugc_season_dict["cover"]
        self.Mid:        int = ugc_season_dict["mid"]
        self.Intro:      str = ugc_season_dict["intro"] # 合集简介
        self.SignState:  int = ugc_season_dict["sign_state"]
        self.Attribute:  int = ugc_season_dict["attribute"]
        self.Sections:   List[UgcSection] = UgcSection.UgcSectionList(ugc_season_dict["sections"])
        self.Stat:       UgcStat          = UgcStat(ugc_season_dict["stat"])
        self.EpCount:    int              = ugc_season_dict["ep_count"] # 合集数量
        self.SeasonType: int              = ugc_season_dict["season_type"]