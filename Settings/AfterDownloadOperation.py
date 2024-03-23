import enum

class AfterDownloadOperation(enum.Enum):
    NONE         = 1
    OPEN_FOLDER  = 2
    CLOSE_APP    = 3
    CLOSE_SYSTEM = 4