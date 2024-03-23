import enum

class FileNamePart(enum.Enum):
    # Video
    ORDER         = 1
    SECTION       = 2
    MAIN_TITLE    = 3
    PAGE_TITLE    = 4
    VIDEO_ZONE    = 5
    AUDIO_QUALITY = 6
    VIDEO_QUALITY = 7
    VIDEO_CODEC   = 8

    # 斜杠
    SLASH         = 100

    # HyphenSeparated
    UNDERSCORE    = 101 # 下划线
    HYPHEN        = 102 # 连字符
    PLUS          = 103 # 加号
    COMMA         = 104 # 逗号
    PERIOD        = 105 # 句号
    AND           = 106 # and
    NUMBER        = 107 # #
    OPEN_PAREN    = 108 # 左圆括号
    CLOSE_PAREN   = 109 # 右圆括号
    OPEN_BRACKET  = 110 # 左方括号
    CLOSE_BRACKET = 111 # 右方括号
    OPEN_BRACE    = 112 # 左花括号
    CLOE_BRACE    = 113 # 右花括号
    BLANK         = 114 # 空白符
