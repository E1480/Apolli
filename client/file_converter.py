import os
from enum import Enum
from typing import Any

import ffmpeg
import pypandoc
from PIL import Image
from pydub import AudioSegment


class FileTypes(Enum):
    # Removed those two because they are more complicated
    #  than I though, and the Archive is like... built-in
    #  why would you do it online?

    Images = "Images"
    Videos = "Videos"
    Audio = "Audio"
    Documents = "Documents"  # Fuck pdfs, why do I need to download LaTex? fuck off.
    Spreadsheet = "Spreadsheet"
    # Presentation = "Presentation"
    Ebook = "Ebook"
    # Archive = "Archive"


# For future me maybe find an executable somewhere to convert
# document to PDF.


# I might be able to turn this into a package 👀
class FilesConverter:
    def __init__(self, file: str, format: str) -> None:
        self.file = file
        self.format = format
        self.output_path = os.path.splitext(file)[0] + "." + format
        self.absoutput = os.path.abspath(self.output_path)

    def VideoConverter(self) -> str:
        ffmpeg.input(self.file).output(self.output_path).run()
        return self.absoutput

    def ImageConverter(self) -> str:
        img = Image.open(os.path.abspath(self.file))
        if self.format in ["jpg", "jpeg"]:
            img.convert("RGB").save(self.absoutput, "JPEG")
        else:
            img.save(os.path.abspath(self.absoutput))

        return os.path.abspath(self.absoutput)

    def AudioConverter(self) -> str:
        audio = AudioSegment.from_file(self.file)

        # pydub uses different format names for some containers
        # Welp that's what I get for being lazy
        fmt_map = {
            "m4a": "ipod",
            "mp3": "mp3",
            "ogg": "ogg",
            "flac": "flac",
            "wav": "wav",
            "aac": "adts",
            "opus": "opus",
            "wma": "asf",  # as fuuuu!
        }

        export_format = fmt_map.get(self.format, self.format)
        audio.export(self.output_path, format=export_format)
        return self.absoutput

    def DocumentConverter(self) -> str:
        pypandoc.convert_file(self.absoutput, self.format, outputfile=self.absoutput)
        return self.absoutput

    def SpreadSheetsConverter(self) -> str:
        ...
        # return os.path.abspath(output_path)

    def EbookConverter(self) -> str:
        ...
        # return os.path.abspath(output_path)


def Convert(file: str, format: Any, type: Any | FileTypes) -> str:

    c = FilesConverter(file, format)

    if type == FileTypes.Videos.name:
        return c.VideoConverter()
    if type == FileTypes.Images.name:
        return c.ImageConverter()
    if type == FileTypes.Audio.name:
        return c.AudioConverter()
    if type == FileTypes.Documents.name:
        return c.DocumentConverter()

    return ""
