from typing import List
from Aria2cNet.Server.AriaConfigFileAllocation import AriaConfigFileAllocation
from Aria2cNet.Server.AriaConfigLogLevel       import AriaConfigLogLevel

class AriaConfig:
    def __init__(self):
        self.ListenPort:              int                      = None # 服务器端口号，取值：1024 - 65535
        self.Token:                   str                      = None # 连接服务器的token
        self.LogLevel:                AriaConfigLogLevel       = None # 日志等级，debug info notice warn error
        self.MaxConcurrentDownloads:  int                      = None # 最大同时下载数（任务数），取值：1 - *
        self.MaxConnecttionPerServer: int                      = None # 同服务器连接数，取值：1 - 16
        self.Split:                   int                      = None # 单文件最大线程数，取值：1 - *
        self.MinSplitSize:            int                      = None # 最小文件分片大小，下载线程数上限取决于能分出多少片，对于小文件重要，单位MB
        self.MaxOverallDownloadLimit: int                      = None # 下载速度限制，取值：1 - *
        self.MaxDownloadLimit:        int                      = None # 下载单文件速度限制，取值：1 - *
        self.MaxOverallUploadLimit:   int                      = None # 上传速度限制，取值：1 - *
        self.MaxUploadLimit:          int                      = None # 上传单文件速度限制，取值：1 - *
        self.ContinueDownload:        bool                     = None # 断点续传
        self.FileAllocation:          AriaConfigFileAllocation = None # 文件预分配，none prealloc
        self.Headers:                 List[str]                = None