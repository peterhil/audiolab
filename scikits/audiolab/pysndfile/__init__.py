# For relative imports to work in Python 3.6
import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from _sndfile import Sndfile, Format, available_file_formats, available_encodings
from compat import formatinfo, sndfile, PyaudioException, PyaudioIOError
from compat import supported_format, supported_endianness, supported_encoding
