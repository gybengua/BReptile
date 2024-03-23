from BiliApi.BiliUtils.ParseEntrance       import ParseEntrance
from BiliApi.Video.VideoInfo               import VideoInfo
from BiliApi.VideoStream.VideoStream       import VideoStream
from Services.Download.AriaDownloadService import AriaDownloadService

from Services.Utils import Utils

class VideoInfoService:
    def __init__(self, input: str):
        if input==None or input=="":
            pass

        if ParseEntrance.IsAvId(input) or ParseEntrance.IsAvUrl(input):
            avid = ParseEntrance.GetAvId(input)
            self.videoView = VideoInfo.VideoViewInfo(None, avid)
        elif ParseEntrance.IsBvId(input) or ParseEntrance.IsBvUrl(input):
            bvid = ParseEntrance.GetBvId(input)
            self.videoView = VideoInfo.VideoViewInfo(bvid)

    def GetVieoStream(self):
        for video_page in self.videoView.Pages:
            play_url = VideoStream.GetVideoPlayUrl(self.videoView.Aid, self.videoView.Bvid, video_page.Cid)
            Utils.VideoPageInfo(play_url, video_page)


if __name__ == '__main__':
    downloadService = AriaDownloadService()
    downloadService.Start()

#vis = VideoInfoService("https://www.bilibili.com/video/BV1RM4y1u7v8/")
#vis.GetVieoStream()
