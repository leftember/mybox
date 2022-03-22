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
         self.health = [] # determine the leaf.
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
        queue = [self.root]
        while len(queue) > 0:
            t = queue.pop(0)
            for i in range(26):
                if t.nodes[i]:
                    if t == self.root:
                        t.nodes[i].end = self.root
                    else:
                        mm = t.end
                        while mm != self.root and not mm.nodes[i]:
                            mm = mm.end
                        if mm == self.root:
                            t.nodes[i].end = self.root
                        else:
                            t.nodes[i].end = mm.nodes[i]
                    queue.append(t.nodes[i])

    def insert(self, s, oindex):
        n = self.root
        for cc in s:
            index = ord(cc) - 97
            if not n.nodes[index]:
                n.nodes[index] = node()
            n = n.nodes[index]
        n.health.append(oindex)

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
                for hi in m.health:
                    if hi >= first and hi <= last:
                        score += self.HHH[hi]
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

    #print(list(map(len, genes)))

    for s_itr in range(s):
        first, last, d = input().split()
        #print(d)
        sss = tree.search_text(d, int(first), int(last))
        #print(first, last, '->', sss)
        low, high = min(low, sss), max(high, sss)
    print(f'{low} {high}')

