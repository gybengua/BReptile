import os
from Storage.Constant import Constant

class StorageManager(object):
    # 若文件夹不存在，则创建文件夹
    @classmethod
    def __CreateDirectory__(cls, directory) -> str:
        if not os.path.exists(directory):
            os.makedirs(directory)
        return directory

    # 获取历史记录的文件路径
    @classmethod
    def GetAriaDir(cls) -> str:
        cls.__CreateDirectory__(Constant.Aria)
        return Constant.Aria

    # 获取历史记录的文件路径
    @classmethod
    def GetDownload(cls) -> str:
        cls.__CreateDirectory__(Constant.Database)
        return Constant.Download

    # 获取历史记录的文件路径
    @classmethod
    def GetHistory(cls) -> str:
        cls.__CreateDirectory__(Constant.Database)
        return Constant.History

    # 获取设置的文件路径
    @classmethod
    def GetSettings(cls) -> str:
        cls.__CreateDirectory__(Constant.Config)
        return Constant.Settings

    # 获取登录cookies的文件路径
    @classmethod
    def GetLogin(cls) -> str:
        cls.__CreateDirectory__(Constant.Config)
        return Constant.Login

    # 获取弹幕的文件夹路径
    @classmethod
    def GetDanmaku(cls) -> str:
        return cls.__CreateDirectory__(Constant.Danmaku)

    # 获取头图的文件夹路径
    @classmethod
    def GetToutu(cls) -> str:
        return cls.__CreateDirectory__(Constant.Toutu)

    # 获取封面的文件夹路径
    @classmethod
    def GetCover(cls) -> str:
        return cls.__CreateDirectory__(Constant.Cover)

    # 获取封面索引的文件路径
    @classmethod
    def GetCoverIndex(cls) -> str:
        cls.__CreateDirectory__(Constant.Cover)
        return Constant.CoverIndex

    # 获取视频快照的文件夹路径
    @classmethod
    def GetSnapshot(cls) -> str:
        return cls.__CreateDirectory__(Constant.Snapshot)

    # 获取视频快照索引的文件路径
    @classmethod
    def GetSnapshotIndex(cls) -> str:
        cls.__CreateDirectory__(Constant.Snapshot)
        return Constant.SnapIndex

    # 获取用户头像的文件夹路径
    @classmethod
    def GetHeader(cls) -> str:
        return cls.__CreateDirectory__(Constant.Header)

    # 获取用户头像索引的文件路径
    @classmethod
    def GetHeaderIndex(cls) -> str:
        cls.__CreateDirectory__(Constant.Header)
        return Constant.HeaderIndex