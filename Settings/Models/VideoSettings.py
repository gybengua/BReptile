from typing import List
from Settings.VideoCodecs  import VideoCodecs
from Settings.AllowStatus  import AllowStatus
from FileName.FileNamePart import FileNamePart

class VideoSettings:
    def __init__(self):
        self.VideoCodecs:           VideoCodecs        = VideoCodecs.NONE
        self.Quality:               int                = 0
        self.AudioQuality:          int                = 0
        self.IsTranscodingFlvToMp4: AllowStatus        = AllowStatus.NONE
        self.SaveVideoRootPath:     str                = ""
        self.HistoryVideoRootPaths: List[AllowStatus]  = None
        self.FileNameParts:         List[FileNamePart] = None