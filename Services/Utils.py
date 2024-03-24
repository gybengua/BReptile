from Settings.SettingsManager import SettingsManager
from BiliApi.BiliUtils.Constant import Constant
from ViewModels.VideoQuality import VideoQuality
from Settings.VideoCodecs import VideoCodecs
from CoreUtils.Format import Format

class Utils:
    @classmethod
    def VideoPageInfo(cls, playUrl, page):
        if playUrl == None:
            return None

        page.PlayUrl        = playUrl
        userInfo            = SettingsManager.GetInstance().GetUserInfo()
        defaultQuality      = SettingsManager.GetInstance().GetQuality()
        videoCodecs         = SettingsManager.GetInstance().GetVideoCodecs()
        defaultAudioQuality = SettingsManager.GetInstance().GetAudioQuality()

        # 未登录时，最高仅720P
        if userInfo.Mid==None or userInfo.Mid==-1:
            if defaultQuality > 64:
                defaultQuality = 64

        # 非大会员账号登录时，如果设置的画质高于1080P，则这里限制为1080P
        if userInfo.IsVip==None or userInfo.IsVip==False:
            if defaultQuality > 80:
                defaultQuality = 80

        if playUrl.Durl != None:
            return

        if playUrl.Dash != None:
            # 如果video列表或者audio列表没有内容，则返回
            if playUrl.Dash.Video == None:
                return
            if (playUrl.Dash.Video) == 0:
                return

            # 音质
            page.AudioQualityFormatList = cls.GetAudioQualityFormatList(playUrl, defaultAudioQuality)
            if len(page.AudioQualityFormatList) > 0:
                page.AudioQualityFormat = page.AudioQualityFormatList[0]

            # 画质 & 视频编码
            page.VideoQualityList = cls.GetVideoQualityList(playUrl, userInfo, defaultQuality, videoCodecs)
            if len(page.VideoQualityList) > 0:
                page.VideoQuality = page.VideoQualityList[0]

            # 时长
            page.Duration = Format.FormatDuration(playUrl.Dash.Duration)

    @classmethod
    def GetAudioQualityFormatList(cls, playUrl, defaultAudioQuality):
        if playUrl.Dash.Audio == None:
            return []

        audioQualityFormatList = []
        for audio in playUrl.Dash.Audio:
            # 音质id大于设置画质时，跳过
            if audio.Id > defaultAudioQuality:
                continue

            audioQuality = Constant.qualities.get(audio.Id, None)
            audioQualityFormatList.append(audioQuality)

        audioQualityFormatList.sort(key=lambda quality : quality.Id, reverse=True)

        return audioQualityFormatList

    @classmethod
    def GetVideoQualityList(cls, playUrl, userInfo, defaultQuality, videoCodecs):
        if playUrl.Dash.Video == None:
            return []

        videoQualityDict = dict()
        for video in playUrl.Dash.Video:
            # 画质id大于设置画质时，跳过
            if video.Id > defaultQuality:
                continue

            # 非大会员账户登录
            if userInfo.IsVip==None or userInfo.IsVip==False:
                # 如果画质为720P60，跳过
                if video.Id == 74:
                    continue

            selectedQuality = playUrl.SupportFormatsDict.get(video.Id, None)
            if selectedQuality != None:
                qualityFormat = selectedQuality.NewDescription

            # 寻找是否已存在这个画质
            # 不存在则添加，存在则修改
            codecName = cls.GetVideoCodecName(video.Codecs)
            videoQualityExist = videoQualityDict.get(video.Id, None)
            if videoQualityExist == None:
                videoCodecList = []
                videoCodecList.append(codecName)

                videoQuality                = VideoQuality()
                videoQuality.quality        = video.Id
                videoQuality.qualityFormat  = qualityFormat
                videoQuality.videoCodecList = videoCodecList

                videoQualityDict[video.Id] = videoQuality
            else:
                if not codecName in videoQualityExist.videoCodecList:
                    videoQualityExist.videoCodecList.append(codecName)

            # 设置选中的视频编码
            selectedVideoQuality = videoQualityDict[video.Id]
            if videoCodecs == VideoCodecs.AVC:
                if "H.264/AVC" in selectedVideoQuality.videoCodecList:
                    selectedVideoQuality.selectedVideoCodec = "H.264/AVC"
            elif videoCodecs == VideoCodecs.HEVC:
                if "H.265/HEVC" in selectedVideoQuality.videoCodecList:
                    selectedVideoQuality.selectedVideoCodec = "H.265/HEVC"

            if len(selectedVideoQuality.videoCodecList) == 1:
                selectedVideoQuality.selectedVideoCodec = selectedVideoQuality.videoCodecList[0]

        return list(videoQualityDict.values())


    # 根据输入的字符串判断是AVC还是HEVC
    @classmethod
    def GetVideoCodecName(cls, origin):
        if origin.__contains__("avc"):
            return "H.264/AVC"
        elif origin.__contains__("hev"):
            return "H.265/HEVC"
        elif origin.__contains__("dvh") or origin.__contains__("hvc"):
            return "Dolby Vision"
        else:
            return ""