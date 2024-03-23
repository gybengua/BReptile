class UserInfoSettings:
    def __init__(self):
        self.Mid:     int  = 0
        self.Name:    str  = ""
        self.IsLogin: bool = False # 是否登录
        self.IsVip:   bool = False # 是否为大会员，未登录时为False