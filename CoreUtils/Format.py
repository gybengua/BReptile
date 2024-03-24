class Format:
    @classmethod
    def FormatDuration(cls, duration):
        if duration // 60 > 0:
            dur = duration // 60
            if dur//60 > 0:
                formatDuration = f"{dur//60}h{dur%60}m{duration%60}s"
            else:
                formatDuration = f"{duration//60}m{duration%60}s"
        else:
            formatDuration = f"{duration}s"

        return formatDuration
