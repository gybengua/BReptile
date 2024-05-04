from typing import List

from BiliApi.Video.Models.UgcSection import UgcSection
from BiliApi.Video.Models.UgcStat import UgcStat


class UgcSeason:
    def __init__(self, ugc_season_dict):
        if ugc_season_dict == None:
            return None

        self.attribute:     int              = ugc_season_dict["attribute"]
        self.cover:         str              = ugc_season_dict["cover"]
        self.ep_count:      int              = ugc_season_dict["ep_count"]
        self.id:            int              = ugc_season_dict["id"]
        self.intro:         str              = ugc_season_dict["intro"]
        self.is_pay_season: bool             = ugc_season_dict["is_pay_season"]
        self.mid:           int              = ugc_season_dict["mid"]
        self.season_type:   int              = ugc_season_dict["season_type"]
        self.sections:      List[UgcSection] = UgcSection.UgcSectionList(ugc_season_dict["sections"])
        self.sign_state:    int              = ugc_season_dict["sign_state"]
        self.stat:          UgcStat          = UgcStat(ugc_season_dict["stat"])
        self.title:         str              = ugc_season_dict["title"]