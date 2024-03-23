from Settings.AfterDownloadOperation import AfterDownloadOperation
from Settings.AllowStatus            import AllowStatus
from Settings.ParseScope             import ParseScope
from Settings.DownloadFinishedSort   import DownloadFinishedSort

class BasicSettings:
    def __init__(self):
        self.AfterDownload:        AfterDownloadOperation = AfterDownloadOperation.NONE
        self.IsListenClipboard:    AllowStatus            = AllowStatus.NONE
        self.IsAutoParseVideo:     AllowStatus            = AllowStatus.NONE
        self.ParseScope:           ParseScope             = ParseScope.NONE
        self.DownloadFinishedSort: DownloadFinishedSort   = DownloadFinishedSort.DOWNLOAD