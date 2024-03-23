from Aria2cNet.Server.AriaConfig import AriaConfig
from Settings.SettingsManager    import SettingsManager
from Aria2cNet.Server.AriaServer import AriaServer

class AriaDownloadService:
    def __init__(self):
        self.retry:    int = 5
        self.nullMark: str = "<null>"

    def StartAriaServer(self):
        header = [
            "Cookie: ",
            "Origin: https://www.bilibili.com",
            "Referer: https://www.bilibili.com",
            "User-Agent:  Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
        ]
        config                         = AriaConfig()
        config.ListenPort              = SettingsManager.GetInstance().GetAriaListenPort()
        config.Token                   = "downkyi"
        config.LogLevel                = SettingsManager.GetInstance().GetAriaLogLevel()
        config.MaxConcurrentDownloads  = SettingsManager.GetInstance().GetAriaMaxConcurrentDownloads()
        config.MaxConnectionPerServer  = 16 # 最大取16
        config.Split                   = SettingsManager.GetInstance().GetAriaSplit()
        config.MinSplitSize            = 10 # 10MB
        config.MaxOverallDownloadLimit = SettingsManager.GetInstance().GetAriaMaxOverallDownloadLimit()*1024 # 输入的单位是KB/s，所以需要1024
        config.MaxDownloadLimit        = SettingsManager.GetInstance().GetAriaMaxDownloadLimit()*1024 # 输入的单位时KB/s，所以需要乘以1024
        config.MaxOverallUploadLimit   = 0
        config.MaxUploadLimit          = 0
        config.ContinueDownload        = True
        config.FileAllocation          = SettingsManager.GetInstance().GetAriaFileAllocation()
        config.Headers                 = header

        AriaServer.StartServer(config)

    def Start(self):
        self.StartAriaServer()