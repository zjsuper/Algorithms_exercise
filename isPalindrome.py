# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 01:20:19 2017

@author: zjgsw
"""

def isPalindrome(x):
    if x < 0:
        return False
    div = 1
    while x// div >= 10:
        div = div * 10
    while x:
        left = x // div
        right = x % 10
        if left != right:
                return False
        x = ( x % div ) // 10
        div = div / 100
    return True

print(isPalindrome(123321))

#print(123321/10)