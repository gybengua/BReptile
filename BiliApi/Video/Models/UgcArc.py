from BiliApi.Models.VideoOwner import VideoOwner
from BiliApi.Models.Dimension import Dimension
from BiliApi.Video.Models.VideoStat import VideoStat

class UgcArc:
    def __init__(self, ugc_arc_dict):
        self.Aid:       int = ugc_arc_dict["aid"]
        self.Videos:    int = ugc_arc_dict["videos"]
        self.TypeId:    int = ugc_arc_dict["type_id"]
        self.TypeName:  int = ugc_arc_dict["type_name"]
        self.Copyright: int = ugc_arc_dict["copyright"]
        self.Pic:       str = ugc_arc_dict["pic"]
        self.Title:     str = ugc_arc_dict["title"]
        self.Pubdate:   int = ugc_arc_dict["pubdate"]
        self.Ctime:     int = ugc_arc_dict["ctime"]
        self.Desc:      str = ugc_arc_dict["desc"]
        self.State:     int = ugc_arc_dict["state"]
        self.Duration:  int = ugc_arc_dict["duration"]
        self.Author:    VideoOwner = ugc_arc_dict["author"]
        self.Stat:      VideoStat  = ugc_arc_dict["stat"]
        self.Dynamic:   str        = ugc_arc_dict["dynamic"]
        self.Dimension: Dimension  = ugc_arc_dict["dimension"]