class UgcStat:
    def __init__(self, ugc_stat_dict):
        self.coin:      int = ugc_stat_dict["coin"]
        self.danmaku:   int = ugc_stat_dict["danmaku"]
        self.fav:       int = ugc_stat_dict["fav"]
        self.his_rank:  int = ugc_stat_dict["his_rank"]
        self.like:      int = ugc_stat_dict["like"]
        self.now_rank:  int = ugc_stat_dict["now_rank"]
        self.reply:     int = ugc_stat_dict["reply"]
        self.season_id: int = ugc_stat_dict["season_id"]
        self.share:     int = ugc_stat_dict["share"]
        self.view:      int = ugc_stat_dict["view"]
        self.vt:        int = ugc_stat_dict["vt"]
        self.vv:        int = ugc_stat_dict["vv"]