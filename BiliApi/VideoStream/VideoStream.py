import json
import requests
from BiliApi.VideoStream.Models.PlayUrl import PlayUrlOrigin, PlayUrl

class VideoStream:
    @classmethod
    def GetPlayUrl(cls, url):
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
            "referer": "https://www.bilibili.com",
        }

        response        = requests.get(url, headers=headers).text
        play_url_origin = PlayUrlOrigin(json.loads(response))
        if play_url_origin.Data is not None:
            return PlayUrl(play_url_origin.Data)
        elif play_url_origin.Result is not None:
            return PlayUrl(play_url_origin.Result)
        else:
            return None


    @classmethod
    def GetVideoPlayUrl(cls, avid, bvid, cid, quality=125):
        baseUrl = f"https://api.bilibili.com/x/player/playurl?cid={cid}&qn={quality}&fourk=1&fnver=0&fnval=4048"
        if bvid is not None:
            url = f"{baseUrl}&bvid={bvid}"
        elif avid is not None:
            url = f"{baseUrl}&aid={avid}"
        else:
            return None

        return cls.GetPlayUrl(url)