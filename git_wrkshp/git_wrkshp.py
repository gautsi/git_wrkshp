# -*- coding: utf-8 -*-

import numpy as np


def add(a, b):
    '''
    This function adds two numbers.

    :param int a: the first number
    :param int b: the second number

    :returns: the sum of *a* and *b*
    :rtype: int

    For example,

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
