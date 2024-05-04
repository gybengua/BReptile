from typing import List

from BiliApi.Models.Dimension import Dimension
from BiliApi.Models.VideoOwner import VideoOwner
from BiliApi.Video.Models.UgcSeason import UgcSeason
from BiliApi.Video.Models.VideoPage import VideoPage
from BiliApi.Video.Models.VideoStat import VideoStat
from BiliApi.Video.Models.VideoSubtitle import VideoSubtitle

class VideoView:
    def __init__(self, data_dict):
        self.aid:        int             = data_dict["aid"]
        self.bvid:       str             = data_dict["bvid"]
        self.cid:        int             = data_dict["cid"]
        self.copyright:  int             = data_dict["copyright"]
        self.ctime:      int             = data_dict["ctime"]
        self.desc:       str             = data_dict["desc"]
        self.dimension:  Dimension       = Dimension(data_dict["dimension"])
        self.duration:   int             = data_dict["duration"]
        self.dynamic:    str             = data_dict["dynamic"]
        self.mission_id: int             = data_dict["mission_id"]
        self.owner:      VideoOwner      = VideoOwner(data_dict["owner"])
        self.pages:      List[VideoPage] = VideoPage.VideoPageList(data_dict["pages"])
        self.pic:        str             = data_dict["pic"]
        self.pubdate:    int             = data_dict["pubdate"]
        self.season_id:  int             = data_dict["season_id"]
        self.stat:       VideoStat       = VideoStat(data_dict["stat"])
        self.state:      int             = data_dict["state"]
        self.subtitle:   VideoSubtitle   = VideoSubtitle(data_dict["subtitle"])
        self.tid:        int             = data_dict["tid"]
        self.title:      str             = data_dict["title"]
        self.tname:      str             = data_dict["tname"]
        self.ugc_season: UgcSeason       = UgcSeason(data_dict["ugc_season"])
        self.videos:     int             = data_dict["videos"]