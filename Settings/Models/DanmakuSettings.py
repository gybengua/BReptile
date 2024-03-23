from Settings.AllowStatus            import AllowStatus
from Settings.DanmakuLayoutAlgorithm import DanmakuLayoutAlgorithm

class DanmakuSettings:
    def __init__(self):
        self.DanmakuTopFilter:          AllowStatus = AllowStatus.NONE
        self.DanmakuBottomFilter:       AllowStatus = AllowStatus.NONE
        self.DanmakuScrollFilter:       AllowStatus = AllowStatus.NONE
        self.IsCustomDanmakuResolution: AllowStatus = AllowStatus.NONE
        self.DanmakuScreenWidth:        int         = 0
        self.DanmakuScreenHeight:       int         = 0
        self.DanmakuFontName:           str         = None
        self.DanmakuFontSize:           int         = 0
        self.DanmakuLineCount:          int         = 0
        self.DanmakuLayoutAlgorithm:    DanmakuLayoutAlgorithm = DanmakuLayoutAlgorithm.NONE
