from Settings.Models.BasicSettings    import BasicSettings
from Settings.Models.NetworkSettings  import NetworkSettings
from Settings.Models.VideoSettings    import VideoSettings
from Settings.Models.DanmakuSettings  import DanmakuSettings
from Settings.Models.AboutSettings    import AboutSettings
from Settings.Models.UserInfoSettings import UserInfoSettings


class AppSettings:
    def __init__(self):
        self.Basic:    BasicSettings    = BasicSettings()
        self.Network:  NetworkSettings  = NetworkSettings()
        self.Video:    VideoSettings    = VideoSettings()
        self.Danmaku:  DanmakuSettings  = DanmakuSettings()
        self.About:    AboutSettings    = AboutSettings()
        self.UserInfo: UserInfoSettings = UserInfoSettings()
