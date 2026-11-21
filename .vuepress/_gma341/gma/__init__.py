# -*- coding: utf-8 -*-
import os
_here = os.path.dirname(__file__)
_data_path = os.path.join(_here, '_data')
if 'GMA_Data' not in os.environ:
    os.environ['GMA_Data'] = _data_path

if 'PROJ_LIB' not in os.environ:
    os.environ['PROJ_LIB'] = _data_path

_lib_path = os.path.join(_here, '_lib')
if _lib_path not in os.environ['PATH']:
    os.environ['PATH'] = _lib_path + ';' + os.environ['PATH']

os.add_dll_directory(_lib_path)
del os

try:
    from importlib.metadata import version
    __version__ = version(__name__)
except:
    __version__ = "unknown"
finally:
    del version

from ._algos.core import env


