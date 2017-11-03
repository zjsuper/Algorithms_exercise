# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 01:55:27 2017

@author: zjgsw
"""

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x in range(2**(-31),2**31):
        if x >= 0:
            string = str(x)
            list_x =[]
            for i in string:
                list_x.append(int(i))
            k = len(list_x)
            target = 0
            for i in range(k-1,-1,-1):
                target += list_x[i] * (10**i)
            return target
        else:
            x = x * (-1)
            string = str(x)
            list_x =[]
            for i in string:
                list_x.append(int(i))
            k = len(list_x)
            target = 0
            for i in range(k-1,-1,-1):
                target += list_x[i] * (10**i)
            return target*(-1)   
    else:
        return 0