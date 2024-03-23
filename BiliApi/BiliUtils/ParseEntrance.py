import re


class ParseEntrance:
    WwwUrl = "https://www.bilibili.com"
    ShareWwwUrl = "https://www.bilibili.com/s"
    ShortUrl = "https://b23.tv/"
    MobileUrl = "https://m.bilibili.com"
    SpaceUrl = "https://space.bilibili.com"

    VideoUrl = f"{WwwUrl}/video/"
    BangumiUrl = f"{WwwUrl}/bangumi/play/"
    BangumiMediaUrl = f"{WwwUrl}/bangumi/media/"
    CheeseUrl = f"{WwwUrl}/cheese/play/"
    FavoritesUrl1 = f"{WwwUrl}/medialist/detail/"
    FavoritesUrl2 = f"{WwwUrl}/medialist/play/"

    @classmethod
    def __IsUrl__(cls, input_text: str) -> bool:
        return (input_text.startswith("http：//") or input_text.startswith("https://"))

    @classmethod
    def __EnableHttps__(cls, url: str) -> str:
        if not cls.__IsUrl__(url):
            return None
        return url.replace("http://", "https://")

    @classmethod
    def __DeleteUrlParam__(cls, url: str) -> str:
        str_list = url.split("?")
        if str_list[0].endswith("/"):
            return str_list[0].rstrip("/")
        else:
            return str_list[0]

    @classmethod
    def __GetId__(cls, input_text: str, baseUrl: str) -> str:
        if not cls.__IsUrl__(input_text):
            return ""

        url = cls.__EnableHttps__(input_text)
        url = cls.__DeleteUrlParam__(url)
        url = url.replace(cls.ShareWwwUrl, cls.WwwUrl)
        url = url.replace(cls.MobileUrl, cls.WwwUrl)

        if url.find("b23.tv/ss") != -1 or url.find("b23.tv/ep") != -1:
            url = url.replace(cls.ShortUrl, cls.BangumiUrl)
        else:
            url = url.replace(cls.ShortUrl, cls.VideoUrl)

        if not url.startswith(baseUrl):
            return ""

        return url.replace(baseUrl, "")

    @classmethod
    def __GetVideoId__(cls, input_text: str) -> str:
        return cls.__GetId__(input_text, cls.VideoUrl)

    @classmethod
    def __IsIntId__(cls, input_text: str, prefix: str) -> bool:
        if input_text.lower().startswith(prefix):
            if len(re.findall("^\d+$", input_text[2:])) != 0:
                return True
        return False

    @classmethod
    def IsAvId(cls, video_id: str) -> bool:
        return cls.__IsIntId__(video_id, "av")

    @classmethod
    def IsBvId(cls, video_id: str) -> bool:
        return (video_id.startswith("BV") and len(video_id) == 12)

    @classmethod
    def IsAvUrl(cls, input_text: str) -> bool:
        id = cls.__GetVideoId__(input_text)
        return cls.IsAvId(id)

    @classmethod
    def IsBvUrl(cls, input_text: str) -> bool:
        id = cls.__GetVideoId__(input_text)
        return cls.IsBvId(id)

    @classmethod
    def GetAvId(cls, input_text: str) -> str:
        if cls.IsAvId(input_text):
            return int(input_text[2:])
        elif cls.IsAvUrl(input_text):
            return int(cls.__GetVideoId__(input_text)[2:])
        else:
            return -1

    @classmethod
    def GetBvId(cls, input_text: str) -> str:
        if cls.IsBvId(input_text):
            return input_text
        elif cls.IsBvUrl(input_text):
            return cls.__GetVideoId__(input_text)
        else:
            return ""