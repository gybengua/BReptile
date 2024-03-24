from Aria2cNet.Server.AriaConfigFileAllocation import AriaConfigFileAllocation
from Aria2cNet.Server.AriaConfigLogLevel import AriaConfigLogLevel
from FileName.FileNamePart import FileNamePart
from Settings.DanmakuLayoutAlgorithm import DanmakuLayoutAlgorithm
from Settings.Models.UserInfoSettings import UserInfoSettings
from Settings.VideoCodecs import VideoCodecs
from Storage.StorageManager import StorageManager
from Settings.Models.AppSettings import AppSettings

from Settings.AfterDownloadOperation import AfterDownloadOperation
from Settings.AllowStatus import AllowStatus
from Settings.ParseScope import ParseScope
from Settings.DownloadFinishedSort import DownloadFinishedSort

class SettingsManager(object):
    instance = None

    # 获取SettingsManager实例
    @classmethod
    def GetInstance(cls):
        if cls.instance is None:
            cls.instance = SettingsManager()
        return cls.instance

    def __init__(self):
        self.appSettings       = AppSettings()
        self.settingsName: str = StorageManager.GetSettings()

        # basic
        self.afterDownload     = AfterDownloadOperation.NONE
        self.isListenClipboard = AllowStatus.YES
        self.isAutoParseVideo  = AllowStatus.NO
        self.parseScope        = ParseScope.NONE
        self.finishedSort      = DownloadFinishedSort.DOWNLOAD

        # Video
        self.videoCodecs            = VideoCodecs.AVC # 设置优先下载的视频编码
        self.quality                = 120             # 设置优先下载画质
        self.audioQuality           = 30280           # 设置优先下载音质
        self.isTranscodingFlvToMp4  = AllowStatus.YES # 是否下载flv视频后转码为mp4
        self.saveVideoRootPath      = "Media"         # 默认下载目录
        self.historyVideoRootPaths  = []              # 历史下载目录
        self.isUseSaveVideoRootPath = AllowStatus.NO  # 是否使用默认下载目录，如果是，则每次点击下载选中项时不再询问下载目录
        # 文件命名格式
        self.fileNameParts          = [
            FileNamePart.MAIN_TITLE,
            FileNamePart.SLASH,
            #FileNamePart.SECTION,
            #FileNamePart.SLASH,
            FileNamePart.ORDER,
            FileNamePart.HYPHEN,
            FileNamePart.PAGE_TITLE,
            FileNamePart.HYPHEN,
            FileNamePart.VIDEO_QUALITY,
            FileNamePart.HYPHEN,
            FileNamePart.VIDEO_CODEC
        ]

        # Network
        self.isLiftingOfRegion           = AllowStatus.YES         # 是否开启解除地区限制
        self.ariaListenPort              = 6800                    # Aria服务器端口号
        self.ariaLogLevel                = AriaConfigLogLevel.INFO # Aria日志等级
        self.ariaMaxConcurrentDownloads  = 3                       # Aria最大同时下载数（任务数）
        self.ariaSplit                   = 5                       # Aria单文件最大线程数
        self.ariaMaxOverallDownloadLimit = 0                       # Aria下载速递限制
        self.ariaMaxDownloadLimit        = 0                       # Aria下载单文件速度限制
        self.ariaFileAllocation          = AriaConfigFileAllocation.PREALLOC # Aira文件预分配
        # Aria HttpProxy代理
        self.isAriaHttpProxy             = AllowStatus.NO
        self.ariaHttpProxy               = ""
        self.ariaHttpProxyListenPort     = 0

        # Danmaku
        self.danmakuTopFilter          = AllowStatus.NO # 是否屏蔽顶部弹幕
        self.danmakuBottomFilter       = AllowStatus.NO # 是否屏蔽底部弹幕
        self.danmakuScoreFilter        = AllowStatus.NO # 是否屏蔽滚动弹幕
        self.isCustomDanmakuResolution = AllowStatus.NO # 是否自定义分辨率
        self.danmakuScreenWidth        = 1920           # 分辨率-宽
        self.danmakuScreenHeight       = 1080           # 分辨率-高
        self.danmakuFontName           = "黑体"          # 弹幕字体
        self.danmakuFontSize           = 50             # 弹幕字体大小
        self.danmakuLineCount          = 0              # 弹幕限制行数
        self.danmakuLayoutAlgorithm    = DanmakuLayoutAlgorithm.SYNC # 弹幕布局算法

        # UserInfo
        # 登录用户的mid
        self.userInfo         = UserInfoSettings()
        self.userInfo.Mid     = -1
        self.userInfo.Name    = ""
        self.userInfo.IsLogin = False
        self.userInfo.IsVip   = False

        # About
        self.isReceiveBetaVersion = AllowStatus.NO  # 是否接收测试版更新
        self.autoUpdateWhenLaunch = AllowStatus.YES # 是否在启动时自动检查更新

    def GetSettings(self) -> AppSettings:
        return self.appSettings

    def SetSettings(self):
        pass

    def GetAriaListenPort(self):
        if self.GetSettings().Network.ArialistenPort == None:
            self.SetAriaListenPort(self.ariaListenPort)
            return self.ariaListenPort
        else:
            return self.GetSettings().Network.ArialistenPort
    def SetAriaListenPort(self, ariaListenPort):
        self.GetSettings().Network.ArialistenPort = ariaListenPort

    def GetAriaLogLevel(self):
        if self.GetSettings().Network.AriaLogLevel == None:
            self.SetAriaLogLevel(self.ariaLogLevel)
            return self.ariaLogLevel
        else:
            return self.GetSettings().Network.AriaLogLevel

    def SetAriaLogLevel(self, ariaLogLevel):
        self.GetSettings().Network.AriaLogLevel = ariaLogLevel

    def GetAriaMaxConcurrentDownloads(self):
        if self.GetSettings().Network.AriaMaxConcurrentDownloads == None:
            self.SetAriaMaxConcurrentDownloads(self.ariaMaxConcurrentDownloads)
            return self.ariaMaxConcurrentDownloads
        else:
            return self.GetSettings().Network.AriaMaxConcurrentDownloads

    def SetAriaMaxConcurrentDownloads(self, ariaMaxConcurrentDownloads):
        self.GetSettings().Network.AriaMaxConcurrentDownloads = ariaMaxConcurrentDownloads

    def GetAriaSplit(self):
        if self.GetSettings().Network.AriaSplit == None:
            self.SetAriaSplit(self.ariaSplit)
            return self.ariaSplit
        else:
            return self.GetSettings().Network.AriaSplit

    def SetAriaSplit(self, ariaSplit):
        self.GetSettings().Network.AriaSplit = ariaSplit

    def GetAriaMaxOverallDownloadLimit(self):
        if self.GetSettings().Network.AriaMaxOverallDownloadLimit == None:
            self.SetAriaMaxOverallDownloadLimit(self.ariaMaxOverallDownloadLimit)
            return self.ariaMaxOverallDownloadLimit
        else:
            return self.GetSettings().Network.AriaMaxOverallDownloadLimit

    def SetAriaMaxOverallDownloadLimit(self, ariaMaxOverallDownloadLimit):
        self.GetSettings().Network.AriaMaxOverallDownloadLimit

    def GetAriaMaxDownloadLimit(self):
        if self.GetSettings().Network.AriaMaxDownloadLimit == None:
            self.SetAriaMaxDownloadLimit(self.ariaMaxDownloadLimit)
            return self.ariaMaxDownloadLimit
        else:
            return self.GetSettings().Network.AriaMaxDownloadLimit

    def SetAriaMaxDownloadLimit(self, ariaMaxDownloadLimit):
        self.GetSettings().Network.AriaMaxDownloadLimit = ariaMaxDownloadLimit

    def GetAriaFileAllocation(self):
        if self.GetSettings().Network.AriaFileAllocation == None:
            self.SetAriaFileAllocation(self.ariaFileAllocation)
            return self.ariaFileAllocation
        else:
            return self.GetSettings().Network.AriaFileAllocation

    def SetAriaFileAllocation(self, ariaFileAllocation):
        self.GetSettings().Network.AriaFileAllocation = ariaFileAllocation

    def GetUserInfo(self):
        if self.GetSettings().UserInfo == None:
            self.SetUserInfo(self.userInfo)
            return self.userInfo
        else:
            return self.GetSettings().UserInfo

    def SetUserInfo(self, userInfo):
        self.GetSettings().UserInfo = userInfo

    def GetQuality(self) -> int:
        if self.GetSettings().Video.Quality == None:
            self.SetQuality(self.quality)
            return self.quality
        else:
            return self.GetSettings().Video.Quality

    def SetQuality(self, quality):
        self.GetSettings().Video.Quality = quality

    def GetVideoCodecs(self):
        if self.GetSettings().Video.VideoCodecs == None:
            self.SetVideoCodecs(self.videoCodecs)
            return self.videoCodecs
        else:
            return self.GetSettings().Video.VideoCodecs

    def SetVideoCodecs(self, videoCodecs):
        self.GetSettings().Video.VideoCodecs = videoCodecs

    def GetAudioQuality(self):
        if self.GetSettings().Video.AudioQuality == None:
            self.SetAudioQuality(self.audioQuality)
            return self.audioQuality
        else:
            return self.GetSettings().Video.AudioQuality

    def SetAudioQuality(self, audioQuality):
        self.GetSettings().Video.AudioQuality = audioQuality

    def GetFileNameParts(self):
        if self.GetSettings().Video.FileNameParts==None or len(self.GetSettings().Video.FileNameParts)==0:
            self.SetFileNameParts(self.fileNameParts)
            return self.fileNameParts
        else:
            return self.GetSettings().Video.FileNameParts

    def SetFileNameParts(self, fileNameParts):
        self.GetSettings().Video.FileNameParts = fileNameParts
