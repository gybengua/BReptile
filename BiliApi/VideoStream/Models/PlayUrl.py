from typing import List
from BiliApi.VideoStream.Models.PlayUrlDurl import PlayUrlDurl
from BiliApi.VideoStream.Models.PlayUrlDash import PlayUrlDash
from BiliApi.VideoStream.Models.PlayUrlSupportFormat import PlayUrlSupportFormat

class PlayUrlOrigin:
    def __init__(self, play_url_origin_dict):
        self.Data   = play_url_origin_dict.get("data", None)
        self.Result = play_url_origin_dict.get("result", None)

class PlayUrl:
    def __init__(self, play_url_dict):
        self.AcceptDescription: List[str]                  = play_url_dict["accept_description"]
        self.AcceptQuality:     List[int]                  = play_url_dict["accept_quality"]
        self.Durl:              List[PlayUrlDurl]          = PlayUrlDurl.PlayUrlDurlList(play_url_dict.get("durl", None))
        self.Dash:              PlayUrlDash                = PlayUrlDash(play_url_dict["dash"])
        self.SupportFormats:    List[PlayUrlSupportFormat] = PlayUrlSupportFormat.PlayUrlSupportFormatList(play_url_dict["support_formats"])
        self.SupportFormatsDict = dict()
        for supportFormat in self.SupportFormats:
            self.SupportFormatsDict[supportFormat.Quality] = supportFormat