import re
from typing import List
from FileName.FileNamePart import FileNamePart
from FileName.HyphenSeparated import HyphenSeparated

class FileName:
    def __init__(self, nameParts: List[FileNamePart]):
        self.nameParts:    List[FileNamePart] = nameParts
        self.order:        int                = -1
        self.section:      str                = "SECTION"
        self.mainTitle:    str                = "MAIN_TITLE"
        self.pageTitle:    str                = "PAGE_TITLE"
        self.videoZone:    str                = "VIDEO_ZONE"
        self.audioQuality: str                = "AUDIO_QUALITY"
        self.videoQuality: str                = "VIDEO_QUALITY"
        self.videoCodec:   str                = "VIDEO_CODEC"

    def RelativePath(self) -> str:
        path = ""
        for part in self.nameParts:
            if part == FileNamePart.ORDER:
                if self.order != -1:
                    path = path + str(self.order)
                else:
                    path = path + "ORDER"
            elif part == FileNamePart.SECTION:
                path = path + self.section
            elif part == FileNamePart.MAIN_TITLE:
                path = path + self.mainTitle
            elif part == FileNamePart.PAGE_TITLE:
                path = path + self.pageTitle
            elif part == FileNamePart.VIDEO_ZONE:
                path = path + self.videoZone
            elif part == FileNamePart.AUDIO_QUALITY:
                path = path + self.audioQuality
            elif part == FileNamePart.VIDEO_QUALITY:
                path = path + self.videoQuality
            elif part == FileNamePart.VIDEO_CODEC:
                path = path + self.videoCodec

            if part.value >= 100:
                path = path + HyphenSeparated.Hyphen[part.value]

        path = re.sub("//+", "/", path)
        path.lstrip("/").rstrip("/")

        return path
