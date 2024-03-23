class VideoStat:
    def __init__(self, stat_dict):
        self.Aid:        int = stat_dict["aid"]
        self.View:       int = stat_dict["view"]     # 播放数量
        self.Danmaku:    int = stat_dict["danmaku"]  # 弹幕数量
        self.Like:       int = stat_dict["like"]     # 点赞数量
        self.Coin:       int = stat_dict["coin"]     # 投币数量
        self.Favorite:   int = stat_dict["favorite"] # 收藏数量
        self.Share:      int = stat_dict["share"]    # 分享数量
        self.Reply:      int = stat_dict["reply"]    # 评论数量
        self.NowRank:    int = stat_dict["now_rank"]
        self.HisRank:    int = stat_dict["his_rank"]
        self.Dislike:    int = stat_dict["dislike"]
        self.Evaluation: str = stat_dict["evaluation"]
        self.ArgueMsg:   str = stat_dict.get("argue_msg", None)