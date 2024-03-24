from typing import List
from Settings.VideoCodecs  import VideoCodecs
from Settings.AllowStatus  import AllowStatus
from FileName.FileNamePart import FileNamePart

class VideoSettings:
    def __init__(self):
        self.VideoCodecs:           VideoCodecs        = None
        self.Quality:               int                = None
        self.AudioQuality:          int                = None
        self.IsTranscodingFlvToMp4: AllowStatus        = None
        self.SaveVideoRootPath:     str                = None
        self.HistoryVideoRootPaths: List[AllowStatus]  = None
        self.FileNameParts:         List[FileNamePart] = None