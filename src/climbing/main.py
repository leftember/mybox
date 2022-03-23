#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    rank = [ranked[0]]    
    for r in ranked:
        if r != rank[-1]:
            rank.append(r)
    result = []
    steps = [0.9, 0.7, 0.4, 0]  # progressive check.
    last = len(rank) - 1
    reachTop = False
    for p in player:
        if reachTop == True:
            result.append(1)
            continue
        if p < rank[last]:
            result.append(last + 2) # len(rank) - 1 + 1(next) + 1(offset)
            continue
        if p == rank[last]:
            result.append(last + 1) # len(rank) - 1 + 1(next) + 1(offset)
            continue
        nextr = last
        for st in steps:
            nextr = int(last * st)
            if rank[nextr] >= p:
                break
        if rank[nextr] == p:
            result.append(nextr + 1)
            last = nextr
        elif nextr == 0:
            result.append(1)
            reachTop = True
        else:
            # will be in nextr <-> last.
            while last - nextr > 1:
                mid = nextr + (last-nextr) // 2
                if p > rank[mid]:
                    last = mid
                elif p == rank[mid]:
                    nextr = mid
                    break
                else:
                    nextr = mid
            if rank[nextr] == p:
                result.append(nextr + 1)
                last = nextr
            elif rank[last] == p:
                result.append(last + 1)
            else:
                result.append(nextr + 2)
                last = nextr
    return result

if __name__ == '__main__':

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    print('\n'.join(map(str, result)))

