from typing import List
from BiliApi.VideoStream.Models.PlayUrlDashVideo import PlayUrlDashVideo
from BiliApi.VideoStream.Models.PlayUrlDashDolby import PlayUrlDashDolby

class PlayUrlDash:
    def __init__(self, play_url_dash_dict):
        self.Duration: int                    = play_url_dash_dict["duration"]
        self.Video:    List[PlayUrlDashVideo] = PlayUrlDashVideo.PlayUrlDashVideoList(play_url_dash_dict["video"])
        self.Audio:    List[PlayUrlDashVideo] = PlayUrlDashVideo.PlayUrlDashVideoList(play_url_dash_dict["audio"])
        self.Dolby:    PlayUrlDashDolby       = play_url_dash_dict["dolby"]