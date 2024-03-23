from typing import List

class PlayUrlDurl:
    def __init__(self, play_url_durl_dict):
        self.Order: int = play_url_durl_dict["order"]
        self.Length: int = play_url_durl_dict["length"]
        self.Size: int = play_url_durl_dict["size"]
        self.Url: str = play_url_durl_dict["url"]
        self.BackupUrl: List[str] = play_url_durl_dict["backup_url"]

    @classmethod
    def PlayUrlDurlList(cls, play_url_durl_dict_list):
        if play_url_durl_dict_list == None:
            return None

        res = []
        for play_url_durl_dict in play_url_durl_dict_list:
            res.append(PlayUrlDurl(play_url_durl_dict))
        return res