# -*- coding: utf-8 -*-
import os, io, json, glob, re, sqlite3, warnings

from collections import namedtuple, abc
from functools import partial
from itertools import combinations, combinations_with_replacement

import xml.etree.ElementTree as xet

import numpy as np
np.seterr(all = 'ignore')
np.set_printoptions(suppress = True)

# import pandas as pd
# from scipy import special, signal, stats, spatial, optimize, interpolate, linalg

GMA_Data = os.environ['GMA_Data']



