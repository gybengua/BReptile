from typing import List

from BiliApi.Models.Dimension           import Dimension
from BiliApi.Models.VideoOwner          import VideoOwner
from BiliApi.Video.Models.VideoStat     import VideoStat
from BiliApi.Video.Models.VideoPage     import VideoPage
from BiliApi.Video.Models.VideoSubtitle import VideoSubtitle
from BiliApi.Video.Models.UgcSeason     import UgcSeason

class VideoView:
    def __init__(self, data_dict):
        self.Bvid:            str             = data_dict["bvid"]
        self.Aid:             int             = data_dict["aid"]
        self.Videos:          int             = data_dict["videos"]
        self.Tid:             int             = data_dict["tid"]
        self.Tname:           str             = data_dict["tname"]
        self.Copyright:       int             = data_dict["copyright"]
        self.Pic:             str             = data_dict["pic"]  # 封面图片
        self.Title:           str             = data_dict["title"]
        self.Pubdate:         int             = data_dict["pubdate"]
        self.Ctime:           int             = data_dict["ctime"]
        self.Desc:            str             = data_dict["desc"]
        self.State:           str             = data_dict["state"]
        self.Duration:        str             = data_dict["duration"]  # 视频时长 (s)
        self.RedirectUrl:     str             = data_dict.get("redirect_url", None)
        self.MissionId:       int             = data_dict.get("mission_id", None)
        self.Owner:           VideoOwner      = VideoOwner(data_dict["owner"])
        self.Stat:            VideoStat       = VideoStat(data_dict["stat"])
        self.Dynamic:         str             = data_dict["dynamic"]
        self.Cid:             int             = data_dict["cid"]
        self.Dimension:       Dimension       = Dimension(data_dict["dimension"])
        self.SeasonId:        int             = data_dict.get("season_id", None)
        self.FestivalJumpUrl: str             = data_dict.get("festival_jump_url", None)
        self.Pages:           List[VideoPage] = VideoPage.VideoPageList(data_dict["pages"])
        self.Subtitle:        VideoSubtitle   = VideoSubtitle(data_dict["subtitle"])
        self.UgcSeason:       UgcSeason       = UgcSeason(data_dict.get("ugc_season", None))