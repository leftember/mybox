#!/bin/python3

import math
import os
import random
import re
import sys
import datetime

class node:
     def __init__(self, v):
         self.val = v   # shouldn't need this and can combined to next field.
         self.health = None # determine the leaf.
         self.nodes = [None] * 26
         self.end = None
         self.term = []

class trie:
    def __init__(self):
        self.root = node(None)

    def build_tree(self, arr, healths):
        for i in range(len(arr)):
            self.insert(arr[i], healths[i], i)
        # build fail pointers.
        self.root.end = self.root
        queue = [self.root]
        while len(queue) > 0:
            t = queue.pop(0)
            if not t:
                continue
            v = t.val if t.val else ''
            v = v[1:]
            fail_node = self.root
            while v:
                fail_node = self.find_node(v)
                if fail_node:
                   break
                v = v[1:]
            if not fail_node:
                fail_node = self.root
            t.end = fail_node
            t.term = fail_node.term.copy()
            if t.health:
                t.term.append(t)
            for n in t.nodes:
                if n:
                    queue.append(n)

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

    def insert(self, s, h, oindex, i = 0, n = None):
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
                    n.health = {}
                n.health[oindex] = h
                return
            index = ord(s[i+1]) - 97
            if not n.nodes[index]:
                n.nodes[index] = node(s[:i+2])
            self.insert(s, h, oindex, i + 1, n.nodes[index])


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
                n = n.end
            # calcuate matches.
            for m in n.term:
                # print(f'found {m.val} at {m.health}')
                for k in m.health:
                    if first <= k and k <= last:
                        score += m.health[k]
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
    print(f'building {datetime.datetime.now().time()}')
    tree.build_tree(genes, health)
 
    for s_itr in range(s):
        first_multiple_input = input().rstrip().split()

        first = int(first_multiple_input[0])

        last = int(first_multiple_input[1])

        d = first_multiple_input[2]
        print(f'querying {datetime.datetime.now().time()}')
        score = tree.search_text(d, first, last)
        if score > high:
            high = score
        if score < low:
            low = score
    print(f'{low} {high}')

