class UserInfoSettings:
    def __init__(self):
        self.Mid:     int  = None
        self.Name:    str  = None
        self.IsLogin: bool = None # 是否登录
        self.IsVip:   bool = None # 是否为大会员，未登录时为False