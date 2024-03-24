from BiliApi.VideoStream.PlayStreamType import PlayStreamType
from Services.VideoInfoService import VideoInfoService

class AddToDownloadService:
    def __init__(self, streamType: PlayStreamType):
        if streamType == PlayStreamType.VIDEO:
            self.videoInfoService = VideoInfoService(None)

    def SetDirectory(self):
        self.downloadAudio    = True
        self.downloadVideo    = True
        self.downloadDanmaku  = True
        self.downloadSubtitle = True
        self.downloadCover    = True
        return "."
