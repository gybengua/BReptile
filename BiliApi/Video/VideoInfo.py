import json
import requests
from BiliApi.Video.Models.VideoView import VideoView

class VideoInfo(object):
    @classmethod
    def VideoViewInfo(cls, bvid: str=None, aid: int=-1):
        # https://api.bilibili.com/x/web-interface/view/detail?bvid=BV1Sg411F7cb&aid=969147110&need_operation_card=1&web_rm_repeat=1&need_elec=1&out_referer=https%3A%2F%2Fspace.bilibili.com%2F42018135%2Ffavlist%3Ffid%3D94341835
        baseUrl = "https://api.bilibili.com/x/web-interface/view"
        url = ""
        if bvid != None:
            url = f"{baseUrl}?bvid={bvid}"
        elif aid > -1:
            url = f"{baseUrl}?aid={aid}"
        else:
            return None

        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
            "referer": "https://www.bilibili.com",
        }

        response  = requests.get(url, headers=headers).text
        videoView = VideoView(json.loads(response)["data"])

        return videoView