import os
from enum import Enum
from typing import Any

import ffmpeg


class FileTypes(Enum):
    Images = "Images"
    Videos = "Videos"
    Audio = "Audio"
    Documents = "Documents"
    Spreadsheet = "Spreadsheet"
    Presentation = "Presentation"
    Ebook = "Ebook"
    Archive = "Archive"


def VideoConverter(file: str, format: str) -> str:
    output_path = os.path.splitext(file)[0] + "." + format
    print(f"Converting {file} -> {output_path}")  # debug
    ffmpeg.input(file).output(output_path).run()
    return os.path.abspath(output_path)


def Convert(file: str, format: Any, type: Any | FileTypes) -> str:

    if type == FileTypes.Videos.name:
        return VideoConverter(file, format)
    if type == FileTypes.Images.name:
        print(file)

    return ""
