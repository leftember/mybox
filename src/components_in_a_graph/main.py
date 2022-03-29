#!/bin/python3

import math
import os
import random
import re
import sys

from collections import deque

#
# Complete the 'componentsInGraph' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY gb as parameter.
#

def componentsInGraph(gb):
    # Write your code here
    collected = []
    for g in gb:
        fromset = None
        toset = None
        for c in collected:
            if g[0] in c:
                fromset = c
                break
        for c in collected:
            if g[1] in c:
                toset = c
                isnew = False
                break
        if fromset and toset and fromset is not toset:
            fromset.update(toset)
            collected.remove(toset)
        elif fromset:
            fromset.add(g[1])
        elif toset:
            toset.add(g[0])            
        else:
            collected.append(set([g[0],g[1]]))
    minv, maxv = float('inf'),2
    for c in collected:
        lc = len(c)
        minv = min(minv, lc)
        maxv = max(maxv, lc)
    # print(collected)
    return [minv, maxv]    

if __name__ == '__main__':

    n = int(input().strip())

    gb = []

    for _ in range(n):
        gb.append(list(map(int, input().rstrip().split())))

    result = componentsInGraph(gb)

    print(result)


