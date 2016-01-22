# -*- coding: utf-8 -*-

import numpy as np


def add(a, b):
    '''
    >>> add(2, 3)
    6
    '''
    return func(a, b)


def func(a, b):
    '''
    >>> func(2, 3)
    6
    '''
    return np.prod([a, b])
