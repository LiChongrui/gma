# -*- coding: utf-8 -*-

from ..core import np, namedtuple, error, env
from ..arrmt import to_numeric_array, to_arrays, to_num_arrays_with_same_shape, axis_init
from scipy import stats, special, signal
import pandas as pd

def is_leap(Year):
    """判断是否为如年！"""
    if isinstance(Year, int) is False:
        raise error.ClimetError('The year should be an integer!')
    return Year % 4 == 0 and (Year % 100 != 0 or Year % 400 == 0)



