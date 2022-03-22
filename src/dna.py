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
         self.term = []

class trie:
    def __init__(self):
        self.root = node()
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
                        #print(f'pointing  to {i}')
                        if v.health:
                            v.term.append(v)
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
                    #print(f'pointing to {i}  {v.end.term} ')
                    v.term = v.end.term.copy()
                    if v.health:
                        v.term.append(v)
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
            n.health = [[oindex], [self.HHH[oindex]]]
        else:
            #n.health.append((oindex, self.HHH[oindex]+ n.health[-1][1]))
            n.health[0].append(oindex)
            n.health[1].append(self.HHH[oindex] + n.health[1][-1])

    def search_text(self, text, first, last):
        score = 0
        n = self.root
        for cc in text:
            index = ord(cc) - 97
            while True:
                if n.nodes[index]:
                    n = n.nodes[index]
                    break
                if n == self.root:
                    break
                n = n.end
            # calcuate matches.
            for m in n.term:
                #print(f'found in gene: {m.health} --- {first}----{last}')
                ids,hs = m.health
                left = bisect.bisect_left(ids, first)
                if left >= len(ids):
                    continue
                right = bisect.bisect_right(ids, last)
                #print(left, right, hs)
                score += hs[right-1]
                if left != right - 1:
                    score -= hs[left]
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

    for s_itr in range(s):
        first, last, d = input().split()
        #print(d)
        sss = tree.search_text(d, int(first), int(last))
        low, high = min(low, sss), max(high, sss)
    print(f'{low} {high}')

