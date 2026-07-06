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


def VideoConverter(file: str, format: str) -> str:
    ffmpeg.input(file).output(output_path).run()
    return os.path.abspath(output_path)


def ImageConverter(file: str, format: str) -> str:
    img = Image.open(os.path.abspath(file))
    if format in ["jpg", "jpeg"]:
        img.convert("RGB").save(os.path.abspath(output_path), "JPEG")
    else:
        img.save(os.path.abspath(output_path))

    return os.path.abspath(output_path)


def AudioConverter(file: str, format: str) -> str:
    audio = AudioSegment.from_file(os.path.abspath(file))

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

    export_format = fmt_map.get(format, format)
    audio.export(output_path, format=export_format)
    return os.path.abspath(output_path)


def DocumentConverter(file: str, format: str) -> str:
    pypandoc.convert_file(
        os.path.abspath(file), format, outputfile=os.path.abspath(output_path)
    )

    return os.path.abspath(output_path)


def SpreadSheetsConverter(file: str, format: str) -> str:
    ...
    # return os.path.abspath(output_path)


def EbookConverter(file: str, format: str) -> str:
    ...
    # return os.path.abspath(output_path)


def Convert(file: str, format: Any, type: Any | FileTypes) -> str:

    global output_path  # Idk why I did this, but it works
    output_path = os.path.splitext(file)[0] + "." + format

    if type == FileTypes.Videos.name:
        return VideoConverter(file, format)
    if type == FileTypes.Images.name:
        return ImageConverter(file, format)
    if type == FileTypes.Audio.name:
        return AudioConverter(file, format)
    if type == FileTypes.Documents.name:
        return DocumentConverter(file, format)

    return ""
