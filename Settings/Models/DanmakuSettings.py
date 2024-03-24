from Settings.AllowStatus            import AllowStatus
from Settings.DanmakuLayoutAlgorithm import DanmakuLayoutAlgorithm

class DanmakuSettings:
    def __init__(self):
        self.DanmakuTopFilter:          AllowStatus = None
        self.DanmakuBottomFilter:       AllowStatus = None
        self.DanmakuScrollFilter:       AllowStatus = None
        self.IsCustomDanmakuResolution: AllowStatus = None
        self.DanmakuScreenWidth:        int         = None
        self.DanmakuScreenHeight:       int         = None
        self.DanmakuFontName:           str         = None
        self.DanmakuFontSize:           int         = None
        self.DanmakuLineCount:          int         = None
        self.DanmakuLayoutAlgorithm:    DanmakuLayoutAlgorithm = None
