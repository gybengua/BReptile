class PlayUrlSupportFormat:
    def __init__(self, play_url_support_format_dict):
        self.Quality:        int = play_url_support_format_dict["quality"]
        self.Format:         str = play_url_support_format_dict["format"]
        self.NewDescription: str = play_url_support_format_dict["new_description"]
        self.DisplayDesc:    str = play_url_support_format_dict["display_desc"]
        self.Superscript:    str = play_url_support_format_dict["superscript"]

    @classmethod
    def PlayUrlSupportFormatList(cls, play_url_support_format_dict_list):
        if play_url_support_format_dict_list == None:
            return None

        res = []
        for play_url_support_format_dict in play_url_support_format_dict_list:
            res.append(PlayUrlSupportFormat(play_url_support_format_dict))
        return res