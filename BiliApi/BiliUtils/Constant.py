from BiliApi.BiliUtils.Quality import Quality

class Constant:
    resolutions = {
        127: Quality(Name="超高清 8K", Id=127),
        126: Quality(Name="杜比视界",  Id=126),
        125: Quality(Name="HDR 真彩", Id=125),
        120: Quality(Name="4K 超清",  Id=120),
        116: Quality(Name="1080P 60帧", Id=116),
        112: Quality(Name="1080P 高码率", Id=112),
         80: Quality(Name="1080P 高清", Id=80),
         74: Quality(Name="720P 60帧", Id=74),
         64: Quality(Name="720P 高清", Id=64),
         32: Quality(Name="480P 清晰", Id=32),
         16: Quality(Name="360P 流畅", Id=16)
    }

    qualities = {
        30216: Quality(Name="64K",         Id=30216),
        30232: Quality(Name="132K",        Id=30232),
        30280: Quality(Name="192K",        Id=30280),
        30250: Quality(Name="Dolby Atmos", Id=30250)
    }