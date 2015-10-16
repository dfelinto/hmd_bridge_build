"""
Bridge
======
"""
import struct
import os
import sys

from .dylibs import load_library

def load(name, win_lib=None, linux_lib=None, osx_lib=None):

    suffix = "-x86"
    prefix = "win32"
    file = win_lib

    if 64 == 8 * struct.calcsize("P"):
        suffix = "-x86-64"

    if ("linux" in sys.platform and linux_lib):
        file = linux_lib
        prefix = "linux"

    elif ("darwin" in sys.platform and osx_lib):
        file = osx_lib
        prefix = "darwin"

    libfile = os.path.join(os.path.dirname(os.path.abspath(__file__)), prefix + suffix, file)
    if os.path.isfile(libfile):
        lib = load_library(libfile)

        # make it accessible for this package files
        sys.modules[name] = lib
    else:
        print("lib \"{0}\" not found".format(lib))


load('bridge_wrapper', win_lib='BridgeLib.dll')
load('oculus_legacy_base', win_lib='OculusVR.dll', linux_lib='libOculusVR.so', osx_lib='libOculusVR.dylib')
