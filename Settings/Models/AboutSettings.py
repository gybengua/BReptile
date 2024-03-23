from Settings.AllowStatus import AllowStatus

class AboutSettings(object):
    def __init__(self):
        self.IsReceiveBetaVersionVersion: AllowStatus = AllowStatus.NONE
        self.AutoUpdateWhenLaunch:        AllowStatus = AllowStatus.NONE