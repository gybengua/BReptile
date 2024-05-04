from BiliApi.Video.Models.UgcArc import UgcArc
from BiliApi.Video.Models.VideoPage import VideoPage


class UgcEpisode:
    def __init__(self, ugc_episode_dict):
        self.aid:        int       = ugc_episode_dict["aid"]
        self.arc:        UgcArc    = UgcArc(ugc_episode_dict["arc"])
        self.attribute:  int       = ugc_episode_dict["attribute"]
        self.bvid:       str       = ugc_episode_dict["bvid"]
        self.cid:        int       = ugc_episode_dict["cid"]
        self.id:         int       = ugc_episode_dict["id"]
        self.page:       VideoPage = VideoPage(ugc_episode_dict["page"])
        self.season_id:  int       = ugc_episode_dict["season_id"]
        self.section_id: int       = ugc_episode_dict["section_id"]
        self.title:      str       = ugc_episode_dict["title"]

    @classmethod
    def UgcEpisodeList(cls, ugc_episode_dict_list):
        if ugc_episode_dict_list == None:
            return []
        res = []
        for ugc_episode_dict in ugc_episode_dict_list:
            res.append(UgcEpisode(ugc_episode_dict))
        return res
