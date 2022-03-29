#!/bin/python3

import math
import os
import random
import re
import sys


from collections import deque
#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#

def bfs(n, m, edges, s):
    # Write your code here
    cost = [-1]* (n+1)
    visited = set()
    subs = [e[1] for e in edges if e[0] == s]
    subs.extend([e[0] for e in edges if e[1] == s])
    for sub in subs:
        visited.add(sub)
        cost[sub] = 6
    todo = deque(subs)
    distance = 12
    while len(todo) > 0:
        nexttodo = deque()
        nexttodo.clear()
        for t in todo:
            nextt = [e[1] for e in edges if e[0] == t]
            nextt.extend([e[0] for e in edges if e[1] == t])
            for ntt in nextt:
                if ntt not in visited:
                    cost[ntt] = distance
                    visited.add(ntt)
                    nexttodo.append(ntt)
        todo = nexttodo
        #print(todo)
        distance += 6
    #print(n,m, edges,s)
    #print(cost)
    del cost[s]
    return cost[1:]

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)
        print(result)
