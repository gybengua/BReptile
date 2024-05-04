from BiliApi.Models.Dimension  import Dimension
from BiliApi.Models.VideoOwner import VideoOwner
from BiliApi.Video.Models.VideoStat import VideoStat

class UgcArc:
    def __init__(self, ugc_arc_dict):
        self.aid:       int        = ugc_arc_dict["aid"]
        self.author:    VideoOwner = VideoOwner(ugc_arc_dict["author"])
        self.copyright: int        = ugc_arc_dict["copyright"]
        self.ctime:     int        = ugc_arc_dict["ctime"]
        self.desc:      str        = ugc_arc_dict["desc"]
        self.dimension: Dimension  = Dimension(ugc_arc_dict["dimension"])
        self.duration:  int        = ugc_arc_dict["duration"]
        self.dynamic:   str        = ugc_arc_dict["dynamic"]
        self.pic:       str        = ugc_arc_dict["pic"]
        self.pubdate:   int        = ugc_arc_dict["pubdate"]
        self.stat:      VideoStat  = VideoStat(ugc_arc_dict["stat"])
        self.state:     int        = ugc_arc_dict["state"]
        self.title:     str        = ugc_arc_dict["title"]
        self.type_id:   int        = ugc_arc_dict["type_id"]
        self.type_name: str        = ugc_arc_dict["type_name"]
        self.videos:    int        = ugc_arc_dict["videos"]