from Settings.SettingsManager import SettingsManager

class Utils:
    @classmethod
    def VideoPageInfo(cls, playUrl, page):
        if playUrl == None:
            return None

        page.PlayUrl = playUrl
        userInfo = SettingsManager.GetInstance().GetUserInfo()

        from pprint import pprint
        pprint(vars(userInfo))
