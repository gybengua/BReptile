import enum

class AriaConfigFileAllocation(enum.Enum):
    NONE     = 1 # 没有预分配
    PREALLOC = 2 # 预分配，默认
    FALLOC   = 3 # NTFS建议使用