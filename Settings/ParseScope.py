import enum

class ParseScope(enum.Enum):
    NONE            = 1
    SELECTED_ITEM   = 2
    CURRENT_SECTION = 3
    ALL             = 4