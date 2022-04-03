#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equal' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

mem = {}

def numberof(a, b):
    disatnce = b - a
    if disatnce >= 5:
        times = disatnce // 5
        return times + numberof(a, b- 5 * times)
    elif disatnce == 4:
        return 2
    elif disatnce == 3:
        return 2
    elif disatnce == 2:
        return 1
    elif disatnce == 1:
        return 1
    elif disatnce == 0:
        return 0

def equal(arr, start=0):
    arr = sorted(arr)
    #print('origin', arr[start])
    while start < len(arr) -1 and arr[start] == arr[start+1]:
        start += 1
    if start == len(arr) -1:
        return 0
    # find arr[start] and next number arr[start+1]
    j = start+2
    while j < len(arr) and arr[j] == arr[start + 1]:
        j += 1
    while j < len(arr):
        arr[j] += arr[start+1] - arr[start]
        j += 1
    #print(arr[start], arr[start+1], arr)
    return numberof(arr[start], arr[start+1]) + equal(arr, start+1)

def reset(arr):
    newb = arr[0]
    for i in range(len(arr)):
        arr[i] -= newb

def actionsof(a, b):
    disatnce = b - a
    if disatnce >= 5:
        times = disatnce // 5
        actions = actionsof(a, b - times*5)
        actions[2] += times
        return  actions
    elif disatnce == 4:
        return [0,2,0]
    elif disatnce == 3:
        return [1,1,0]
    elif disatnce == 2:
        return [1,0,0]
    elif disatnce == 1:
        return [1,0,0]
    elif disatnce == 0:
        return [0,0,0]

def equal2(arr, start = 0):
    while start < len(arr) -1 and arr[start] == arr[start+1]:
        start += 1
    if start == len(arr) -1:
        return 0
    # find arr[start] and next number arr[start+1]
    j = start+2
    while j < len(arr):
        arr[j] += arr[start+1] - arr[start]
        j += 1
    #print(arr[start], arr[start+1], arr)
    actions = actionsof(arr[start], arr[start+1])
    print(actions, end = '\t')
    for i in range(start+1):
        arr[i] += arr[start+1] - arr[start]
    reset(arr)
    print(arr)
    return equal2(arr, start+1) + sum(actions)

if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        arr = list(map(int, input().rstrip().split()))
        arr = sorted(arr)
        reset(arr)
        print(arr)
        result = equal2(arr)
        print(result)
