# -*- coding: utf-8 -*-
"""
空间杂项计算。
"""
from ..core import np, combinations_with_replacement, namedtuple, partial, error, env
from ..arrmt import to_numeric_array
from ..geo.crs import CoordinateTransformation, CoordinateReferenceSystem
from ..geo.dataset import Dataset
from ..geo.feature import Feature
from ..geo.layer import Layer
from ..geo.geometry import Geometry
from ..geo.field import FieldType
from ..geo.base import get_xy_resolution, CHARACTERS
from ..core.units import get_unit
from scipy import spatial, optimize, interpolate, linalg
import pandas as pd

EARTH_SEMI_MAJOR = 6378137.0
EARTH_SEMI_MINOR = 6356752.314245179
MEAN_EARTH_SEMI = (EARTH_SEMI_MAJOR * 2 + EARTH_SEMI_MINOR) / 3 

# 克里金法常量
EPS = 1.0e-10
ANISOTROPY_SCALING = 1.0 # 各向异性缩放
ANISOTROPY_ANGLE = 0.0 # 各向异性角

def init_points(points):
    
    if isinstance(points, np.ndarray): 
        if points.ndim == 2 and points.shape[1] == 2:
            return points

    points = np.atleast_2d(points)
    dim = points.ndim
    if dim > 2:
        raise error.SpmisError('X, Y coordinate point format is incorrect!')
    return points[:, :2]

def init_points_and_values(points, values):
    
    points = init_points(points)
    values = to_numeric_array(values).flatten()

    if len(points) != len(values):
        raise error.SpmisError('The number of X, Y points and values entered are not equal!')
    
    return points, values

def init_boundary(boundary):
    
    bou = to_numeric_array(boundary).flatten().tolist()

    if len(bou) != 4:
        raise error.SpmisError(f'Boundary({boundary}) settings (left, bottom, right, top) are incorrect!')
    
    if bou[2] < bou[0] or bou[3] < bou[1]:
        raise error.SpmisError(f'Boundary({boundary}) settings (left < right, bottom < top) are incorrect!')
    
    return boundary



