#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'iterateIt' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def iterateIt(a):
    # Write your code here
    if len(a) == 0:
        return 0
    if len(a) == 1:
        return 1
    rep = 0
    while len(a) > 0:
        done = set()
        for i in range(len(a)):
            for j in range(i+1,len(a)):
                dis = abs(a[j]-a[i])
                if dis != 0 and dis not in done:
                    done.add(dis)
        a = list(done)
        rep += 1
        print(len(done))
    return rep

if __name__ == '__main__':
    a_count = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = iterateIt(a)
    print(result)


