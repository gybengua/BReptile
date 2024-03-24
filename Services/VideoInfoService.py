import os
from BiliApi.BiliUtils.ParseEntrance       import ParseEntrance
from BiliApi.Video.VideoInfo               import VideoInfo
from BiliApi.VideoStream.PlayStreamType import PlayStreamType
from BiliApi.VideoStream.VideoStream       import VideoStream
from Services.Download.AriaDownloadService import AriaDownloadService
from FileName.FileName import FileName

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
    #downloadService = AriaDownloadService()
    #downloadService.Start()
    vis = VideoInfoService("https://www.bilibili.com/video/BV1RM4y1u7v8/")
    vis.GetVieoStream()

    for video_page in vis.videoView.Pages:
        from Settings.SettingsManager import SettingsManager
        fileName = FileName(SettingsManager.GetInstance().GetFileNameParts())
        fileName.order        = video_page.Page
        fileName.mainTitle    = vis.videoView.Title
        fileName.pageTitle    = video_page.Part
        fileName.videoZone    = vis.videoView.Tname
        fileName.audioQuality = video_page.AudioQualityFormat.Name
        fileName.videoQuality = video_page.VideoQuality.qualityFormat
        if video_page.VideoQuality.selectedVideoCodec.__contains__("AVC"):
            fileName.videoCodec = "AVC"
        elif video_page.VideoQuality.selectedVideoCodec.__contains__("HEVC"):
            fileName.videoCodec = "HEVC"
        elif video_page.VideoQuality.selectedVideoCodec.__contains__("Dolby"):
            fileName.videoCodec = "Dolby Vision"
        else:
            fileName.videoCodec = ""

        filePath = os.path.join(".", fileName.RelativePath())

        # 视频类别
        if vis.videoView.Tid == -10:
            playStreamType = PlayStreamType.CHEESE
        elif vis.videoView.Tid ==  13 or \
             vis.videoView.Tid ==  23 or \
             vis.videoView.Tid == 177 or \
             vis.videoView.Tid == 167 or \
             vis.videoView.Tid ==  11:
             playStreamType = PlayStreamType.BANGUMI
        elif vis.videoView.Tid ==   1 or \
             vis.videoView.Tid ==   3 or \
             vis.videoView.Tid == 129 or \
             vis.videoView.Tid ==   4 or \
             vis.videoView.Tid ==  36 or \
             vis.videoView.Tid == 188 or \
             vis.videoView.Tid == 234 or \
             vis.videoView.Tid == 223 or \
             vis.videoView.Tid == 160 or \
             vis.videoView.Tid == 211 or \
             vis.videoView.Tid == 217 or \
             vis.videoView.Tid == 119 or \
             vis.videoView.Tid == 155 or \
             vis.videoView.Tid == 202 or \
             vis.videoView.Tid ==   5 or \
             vis.videoView.Tid == 181:
            playStreamType = PlayStreamType.VIDEO

        temp = filePath.split("/")
        path = filePath.replace(temp[-1], "")
        if not os.path.exists(path):
            os.makedirs(path)


        #from pprint import pprint
        #pprint(vars(vis.videoView))
