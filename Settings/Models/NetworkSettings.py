from Settings.AllowStatus                      import AllowStatus
from Aria2cNet.Server.AriaConfigLogLevel       import  AriaConfigLogLevel
from Aria2cNet.Server.AriaConfigFileAllocation import AriaConfigFileAllocation

class NetworkSettings:
    def __init__(self):
        self.IsLiftingOfRegion:           AllowStatus              = None
        self.ArialistenPort:              int                      = None
        self.AriaLogLevel:                AriaConfigLogLevel       = None
        self.AriaMaxConcurrentDownloads:  int                      = None
        self.AriaSplit:                   int                      = None
        self.AriaMaxOverallDownloadLimit: int                      = None
        self.AriaMaxDownloadLimit:        int                      = None
        self.AriaFileAllocation:          AriaConfigFileAllocation = None
        self.IsAriaHttpProxy:             AllowStatus              = None
        self.AriaHttpProxy:               str                      = None
        self.AriaHttpProxyListenPort:     int                      = None