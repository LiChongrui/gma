# -*- coding: utf-8 -*-

from ..core import np, partial, namedtuple, error, dtypes
from ..core.tools import keep_iterable
from scipy import stats, signal
import pandas as pd

def to_numeric_array(data):
    '''
    Forces the input data to be converted to a numeric array, values that cannot 
    be converted will be modified to nan.

    Parameters
    ----------
    data: All data types.
        Data that needs to be transformed.
    
    Returns
    ----------
    Type: array.
    
    '''
    if isinstance(data, (pd.DataFrame, pd.Series)):
        data = data.values
    elif isinstance(data, np.ndarray) is False:  
        data = np.array(data)
        
    def is_numpy_num(data):
        # 检查是否为数组
        if isinstance(data, np.ndarray) is False:
            return False
        dtype = data.dtype
        if dtype.kind in ('i', 'f', 'c'):
            return True
        else:
            return False
    
    if is_numpy_num(data) is False:
        shape = data.shape
        data = pd.to_numeric(data.ravel(), errors = 'coerce').reshape(shape)
    
    if data.ndim < 1:
        data = np.atleast_1d(data)
    
    return data

def to_arrays(*args):
    '''初始化数组数据。'''
    datas = [to_numeric_array(d) for d in args]
    if len(args) == 1:
        return datas[0]
    else:
        return datas
 
def to_num_arrays_with_same_shape(*args):    
    '''初始化数组数据，并检查结果是否有相同的形状！'''
    datas = to_arrays(args)
    shapes = [d.shape for d in datas]
    if len(set(shapes)) != 1:
        raise error.ArrmtError(f'The data involved in the calculation must have the same shape!'
                               f'Input shape: {shapes}!')
    return datas

def axis_init(data, axis):
    '''通用轴初始化'''
    data = to_numeric_array(data)
    
    if axis is None:
        axis = 0
        data = data.flatten()
    elif isinstance(axis, int):
        if (-data.ndim <= axis < data.ndim) is False:
            raise error.ArrmtError(f'Axis index is out of range! Set value: {axis}!')
        else:
            axis = axis
    else:
        raise error.ArrmtError('Axis type is incorrect!')
    
    return data, axis


