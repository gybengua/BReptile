from Settings.AfterDownloadOperation import AfterDownloadOperation
from Settings.AllowStatus            import AllowStatus
from Settings.ParseScope             import ParseScope
from Settings.DownloadFinishedSort   import DownloadFinishedSort

class BasicSettings:
    def __init__(self):
        self.AfterDownload:        AfterDownloadOperation = None
        self.IsListenClipboard:    AllowStatus            = None
        self.IsAutoParseVideo:     AllowStatus            = None
        self.ParseScope:           ParseScope             = None
        self.DownloadFinishedSort: DownloadFinishedSort   = None