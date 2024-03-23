from typing import List

class PlayUrlDashVideo:
    def __init__(self, play_url_dash_video_dict):
        self.Id: int = play_url_dash_video_dict["id"]
        self.BaseUrl: str = play_url_dash_video_dict["base_url"]
        self.BackupUrl: List[str] = play_url_dash_video_dict["backup_url"]
        self.MimeType: str = play_url_dash_video_dict["mimeType"]
        self.Codecs: str = play_url_dash_video_dict["codecs"]
        self.Width: int = play_url_dash_video_dict["width"]
        self.Height: int = play_url_dash_video_dict["height"]
        self.FrameRate: int = play_url_dash_video_dict["frameRate"]

    @classmethod
    def PlayUrlDashVideoList(cls, play_url_dash_video_dict_list):
        if play_url_dash_video_dict_list == None:
            return None

        res = []
        for play_url_dash_video_dict in play_url_dash_video_dict_list:
            res.append(PlayUrlDashVideo(play_url_dash_video_dict))
        return res