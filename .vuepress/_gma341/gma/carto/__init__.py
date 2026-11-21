# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.markers as mk 
import matplotlib.collections as clt
import matplotlib.axes as axes
import matplotlib.cbook as cbook
import matplotlib.path as mpath
import matplotlib.transforms as mtransforms
import matplotlib.patches as ptc
import matplotlib.colors as cor
import matplotlib.font_manager as ftm
import matplotlib.textpath as tph

import pandas as pd
from .._algos.core import tools, env, dtypes, error, np, env, GMA_Data
from .._algos.core.gdata import const
from .._algos.geo.crs import (create_bou, create_ext, 
                              CoordinateReferenceSystem, CoordinateTransformation, 
                              MapBoundary, 
                              UNIT_DEG_X, UNIT_DEG_Y)

from .._algos.arrmt import to_numeric_array
from .._algos.geo.geometry import Geometry, base_geom_to_points
from .._algos.geo.layer import Layer
from .._algos.geo.feature import Feature
from .._algos.geo.dataset import Dataset, raster_translate, mask_array_nodata
from .._algos.geo.geodatabase import open_file, open_raster
from .._algos.spmis.meatran import Miscellaneous


