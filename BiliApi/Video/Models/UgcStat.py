class UgcStat:
    def __init__(self, ugc_stat_dict):
        self.SeasonId: int = ugc_stat_dict["season_id"]
        self.View: int = ugc_stat_dict["view"]
        self.Danmaku: int = ugc_stat_dict["danmaku"]
        self.Reply: int = ugc_stat_dict["reply"]
        self.Favorite: int = ugc_stat_dict["fav"]
        self.Coin: int = ugc_stat_dict["coin"]
        self.Share: int = ugc_stat_dict["share"]
        self.NowRank: int = ugc_stat_dict["now_rank"]
        self.HisRank: int = ugc_stat_dict["his_rank"]
        self.Like: int = ugc_stat_dict["like"]