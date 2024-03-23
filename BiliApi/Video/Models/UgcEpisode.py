from BiliApi.Video.Models.UgcArc import UgcArc
from BiliApi.Video.Models.VideoPage import VideoPage

class UgcEpisode:
    def __init__(self, ugc_episode_dict):
        self.SeasonId: int = ugc_episode_dict["season_id"]
        self.SectionId: int = ugc_episode_dict["section_id"]
        self.Id: int = ugc_episode_dict["id"]
        self.Aid: int = ugc_episode_dict["aid"]
        self.Cid: int = ugc_episode_dict["cid"]
        self.Title: str = ugc_episode_dict["title"]
        self.Attribute: int = ugc_episode_dict["attribute"]
        self.Arc: UgcArc = UgcArc(ugc_episode_dict["arc"])
        self.Page: VideoPage = VideoPage(ugc_episode_dict["page"])
        self.Bvid: str = ugc_episode_dict["bvid"]

    @classmethod
    def UgcEpisodeList(cls, ugc_episode_dict_list):
        if ugc_episode_dict_list == None:
            return None

        res = []
        for ugc_episode_dict in ugc_episode_dict_list:
            res.append(UgcEpisode(ugc_episode_dict))
        return res