#!/bin/python3

import math
import os
import random
import re
import sys
import datetime
import bisect

class node:
     def __init__(self, v):
         self.val = v # shouldn't need this and can combined to next field.
         self.health = None # determine the leaf.
         self.nodes = [None] * 26
         self.end = None
         self.term = []

class trie:
    def __init__(self):
        self.root = node(None)
        self.HHH = None

    def build_tree(self, arr, healths):
        self.HHH = healths
        for i in range(len(arr)):
            self.insert(arr[i], i)
        # build fail pointers.
        self.root.end = self.root
        queue = [self.root]
        while len(queue) > 0:
            t = queue.pop(0)
            if not t:
                continue
            if t == self.root:
                for i,v in enumerate(t.nodes):
                    if v:
                        v.end = self.root
                        #print(f'pointing {v.val} to {i} {v.end.val}')
                        if v.health:
                            v.term.append(v)
                        queue.append(v)
                continue
            for i,v in enumerate(t.nodes):
                if v:
                    v.end = t.end.nodes[i]
                    #print(f'pointing {v.val} to {i} {v.end.val}')
                    v.term = v.end.term.copy()
                    if v.health:
                        v.term.append(v)
                    queue.append(v)

    def find_node(self, v):
        n = self.root
        while len(v) > 0:
            index = ord(v[0])-97
            nn = n.nodes[index]
            if not nn:
                break
            n = nn
            v = v[1:]
        if len(v) > 0:
            return None
        else:
            return n

    def insert(self, s, oindex, i = 0, n = None):
        if i < len(s):
            if not n: # root node
                n = self.root
                index = ord(s[0]) - 97
                if not n.nodes[index]:
                    n.nodes[index] = node(s[0])
                n = n.nodes[index]
            if i == len(s) -1:
                # the last one
                # print(f'adding {s} {h} at {oindex}')
                if not n.health:
                    n.health = []
                n.health.append(oindex)
                return
            index = ord(s[i+1]) - 97
            if not n.nodes[index]:
                n.nodes[index] = node(s[:i+2])
            self.insert(s, oindex, i + 1, n.nodes[index])

    def search_text(self, text, first, last):
        score = 0
        start = 0
        n = self.root
        while start < len(text):
            index = ord(text[start]) - 97
            while True:
                if n.nodes[index]:
                    n = n.nodes[index]
                    break
                if n == self.root:
                    break
#                print(f'moving to next {n.val}')
                n = n.end
            # calcuate matches.
            for m in n.term:
                #print(f'found {m.val} in gene: {m.health} --- {first}----{last}')
                mlen = len(m.health)
                left = bisect.bisect_left(m.health, first)
                if left >= mlen:
                    continue
                right = bisect.bisect_right(m.health, last)
                if right == 0 and m.health[right] != last:
                    continue
                if right < len(m.health) and  m.health[right] == last:
                    right += 1
                for iii in range(left, right):
                    #print(f'adding {self.HHH[m.health[iii]]}')
                    score += self.HHH[m.health[iii]]
#                rl = len(m.health)
#                left = 0
#                leftv = m.health[left][0]
#                while rl > 1 and leftv < first:
#                    mid = left + rl//2
#                    midv = m.health[mid][0]
#                    if midv > first:
#                        rl = rl // 2
#                    elif midv < first:
#                        ri = rl // 2
#                        left = mid
#                        leftv = m.health[left][0]
#                    else:
#                        left = mid
#                        break
#                if leftv < first:
#                    continue
#                rl = len(m.health)
#                right = rl-1
#                rightv = m.health[right][0]
#                while rl > 1 and rightv > last:
#                    mid = right - rl // 2
#                    midv = m.health[mid][0]
#                    if midv > last:
#                        rl = rl //2
#                        right = mid
#                        rightv = m.health[right][0]
#                    elif midv < last:
#                        ri = rl //2
#                    else:
#                        right = mid
#                        break
#                if rightv > last:
#                    continue
#                for i in range(left, right+1):
#                    print(f'{i}-{m.health[i][1]}')
#                    score += m.health[i][1]
#
                #for k,v in m.health:
                #    if first <= k and k <= last:
                #        score += v
            start += 1
        return score


if __name__ == '__main__':
    n = int(input().strip())
    genes = input().rstrip().split()
    health = list(map(int, input().rstrip().split()))
    s = int(input().strip())
    low = float('inf')
    high = 0
    tree = trie()
    #print(f'building {datetime.datetime.now().time()}')
    tree.build_tree(genes, health)

    for s_itr in range(s):
        first_multiple_input = input().rstrip().split()

        first = int(first_multiple_input[0])

        last = int(first_multiple_input[1])

        d = first_multiple_input[2]
        #print(d)
        score = tree.search_text(d, first, last)
        if score > high:
            high = score
        if score < low:
            low = score
    print(f'{low} {high}')

