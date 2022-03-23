#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridlandProvinces' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def gridlandProvinces2(s, startx, starty):
    # Write your code here
    total = len(s[0]) * 2
    visited = [[0]*len(s[0]), [0]*len(s[0])]
    labels = []
    cur = (startx, starty)
    visited[startx][starty] = 1
    labels.append(cur)
    directions = [0] * (total -1)
    #going next.
    results = set()
    i = 0
    while True:
        if i == len(directions):
            # got one
            # print(labels)
            val = []
            for ll in labels:
                val.append(s[ll[0]][ll[1]])
            results.add(''.join(val))
            i -= 1
            if i == 0:
                break
            visited[cur[0]][cur[1]] = 0
            labels.pop()
            cur = labels[-1]
            directions[i] += 1
        #print(i, directions, visited, labels, '-', cur)
        #print(i)
        if directions[i] == 0:
            # vertical move means half side is already visited.
            if cur[0] > 0 and visited[cur[0]-1][cur[1]] == 0:
                left = True
                for check in range(0, cur[1]):
                    if visited[0][check] == 0 or visited[1][check] == 0:
                        left = False
                        break
                right = True
                for check in range(cur[1]+1, len(s[0])):
                    if visited[0][check] == 0 or visited[1][check] == 0:
                        right = False
                        break
                if not left and not right:
                    directions[i] += 1
                    continue
                cur = (cur[0]-1, cur[1])
                visited[cur[0]][cur[1]] = 1
                labels.append(cur)
                i+=1
            else:
                directions[i] += 1
        elif directions[i] == 1:
            if cur[0] == 0 and visited[cur[0]+1][cur[1]] == 0:
                left = True
                for check in range(0, cur[1]):
                    if visited[0][check] == 0 or visited[1][check] == 0:
                        left = False
                        break
                right = True
                for check in range(cur[1]+1, len(s[0])):
                    if visited[0][check] == 0 or visited[1][check] == 0:
                        right = False
                        break
                if not left and not right:
                    directions[i] += 1
                    continue
                cur = (cur[0]+1, cur[1])
                visited[cur[0]][cur[1]] = 1
                labels.append(cur)
                i+=1
            else:
                directions[i] += 1
        elif directions[i] == 2:
            if cur[1] > 0 and visited[cur[0]][cur[1]-1] == 0:
                cur = (cur[0], cur[1] -1)
                visited[cur[0]][cur[1]] = 1
                labels.append(cur)
                i+=1
            else:
                directions[i] += 1
        elif directions[i] == 3:
            if cur[1] < len(s1)-1 and visited[cur[0]][cur[1]+1] == 0:
                cur = (cur[0], cur[1] + 1)
                visited[cur[0]][cur[1]] = 1
                labels.append(cur)
                i+=1
            else:
                directions[i] += 1
        elif directions[i] == 4:
            # backtrack.
            for j in range(i, len(directions)):
                directions[j] = 0
            if i == 0:
                break
            visited[cur[0]][cur[1]] = 0
            labels.pop()
            cur = labels[-1]
            directions[i-1] += 1
            i -= 1
    return results
    

def gridlandProvinces(s1, s2):
    # Write your code here
    s = [s1, s2]
    results = set()
    for i in range(len(s[0])):
        r = gridlandProvinces2(s, 0, i)
        results.update(r)
        r = gridlandProvinces2(s, 1, i)
        results.update(r)
    # print(results)
    return len(results)
       

if __name__ == '__main__':

    p = int(input().strip())

    for p_itr in range(p):
        n = int(input().strip())

        s1 = input()

        s2 = input()

        result = gridlandProvinces(s1, s2)

        print(str(result) + '\n')


