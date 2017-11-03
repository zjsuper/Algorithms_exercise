# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 01:15:53 2017

@author: zjgsw
"""


def twoSum(nums, target):
    for i in range(len(nums)):
        if (target - nums[i]) in nums:
            for k in range(i+1,len(nums)):
                if nums[k] == (target - nums[i]):
                    return[i,k]
list1 = range(9) 

list2 = range(5,9) 
for i in list2:
    print(i)     
    
    
print(range(10,5,-1))

for i in range(10,-1,-1):
    print(i)
    
    