#!/bin/python3

import math
import os
import random
import re
import sys
import datetime
import bisect

class node:
     def __init__(self):
         self.health = None # determine the leaf.
         self.nodes = [None] * 26
         self.end = None

class trie:
    def __init__(self):
        self.root = node()
        self.HHH = None

    def build_tree(self, arr, healths):
        self.HHH = healths
        for i in range(len(arr)):
            self.insert(arr[i], i)
        # build fail pointers.
        print('insert done')
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
                        queue.append(v)
                continue
            for i,v in enumerate(t.nodes):
                if v:
                    mm = t
                    while not mm.end.nodes[i]:
                        mm = mm.end
                        if mm == self.root:
                            break
                    if mm == self.root:
                        v.end = self.root
                    else:
                        v.end = mm.end.nodes[i]
                    queue.append(v)

    def insert(self, s, oindex):
        n = self.root
        for cc in s:
            index = ord(cc) - 97
            if not n.nodes[index]:
                n.nodes[index] = node()
            n = n.nodes[index]
        if not n.health:
            # presum from start until oindex.
            n.health = [[0], [0]]
        #n.health.append((oindex, self.HHH[oindex]+ n.health[-1][1]))
        n.health[0].append(oindex)
        n.health[1].append(self.HHH[oindex] + n.health[1][-1])

    def search_text(self, text, first, last):
        score = 0
        n = self.root
        for cc in text:
            index = ord(cc) - 97
            while n != self.root and not n.nodes[index]:
                n = n.end
            if not n.nodes[index]:
                continue
            n = n.nodes[index]
            # calcuate matches.
            m = n
            while m != self.root: 
                if m.health:
                #print(f'found in gene: {m.health} --- {first}----{last}')
                    ids,hs = m.health
                    left = bisect.bisect_left(ids, first)
                    if left >= len(ids):
                        continue
                    right = bisect.bisect_right(ids, last)
                    #print(left, right,ids, hs)
                    score += hs[right-1]-hs[left-1 if left > 0 else 0]
                m = m.end
        return score


if __name__ == '__main__':
    n = int(input().strip())
    genes = input().rstrip().split()
    health = list(map(int, input().rstrip().split()))
    s = int(input().strip())
    low = float('inf')
    high = 0
    tree = trie()
    print(f'building {datetime.datetime.now().time()}')
    tree.build_tree(genes, health)
    print('tree done')

    cnt = 0

    for s_itr in range(s):
        first, last, d = input().split()
        #print(d)
        sss = tree.search_text(d, int(first), int(last))
        #print(first, last, '->', sss)
        low, high = min(low, sss), max(high, sss)
        cnt += 1
        if cnt == 2:
            break
    print(f'{low} {high}')

