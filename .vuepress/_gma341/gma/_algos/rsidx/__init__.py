# -*- coding: utf-8 -*-
from ..core import namedtuple, np, error
from ..arrmt import to_num_arrays_with_same_shape

class VIDataPreparation:
    
    def __init__(self, *args):
        '''初始化数据'''
        self._datas = to_num_arrays_with_same_shape(*args)


