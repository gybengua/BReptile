from typing import List
from BiliApi.VideoStream.Models.PlayUrlDashVideo import PlayUrlDashVideo

class PlayUrlDashDolby:
    def __init__(self, play_url_dash_dolby_dict):
        self.Audio: List[PlayUrlDashVideo] = PlayUrlDashVideo.PlayUrlDashVideoList(play_url_dash_dolby_dict["audio"])