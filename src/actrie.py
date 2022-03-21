"""
TriE tree for string search with Aho Corasick mechanism for multi string search.
"""


class node:
     def __init__(self, v):
         self.val = v   # shouldn't need this and can combined to next field.
         self.health = -1 # determine the leaf.
         self.nodes = [None] * 26
         self.fail = None
         self.end = None

class trie:
    indexes = {}
    def __init__(self):
        self.root = node(None)
        #self.indexes = 'aaa' #instance variable can block static variable if present.
        if len(trie.indexes) == 0:
            # initialize
            for i in range(26):
                trie.indexes[chr(ord('a')+i)] = i

    def build_tree(self, arr):
        for s in arr:
            self.insert(s)
        # build fail pointers.
        self.root.fail = self.root
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
            for n in t.nodes:
                if n:
                    n.fail = fail_node
                    queue.append(n)

    def find_node(self, v):
        n = self.root
        while len(v) > 0:
            index = self.indexes[v[0]]
            nn = n.nodes[index]
            if not nn:
                break
            n = nn
            v = v[1:]
        if len(v) > 0:
            return None
        else:
            print('found ' + n.val)
            return n

    def insert(self, s, i = 0, n = None):
        if i < len(s):
            if not n: # root node
                n = self.root
                index = self.indexes[s[0]]
                if not n.nodes[index]:
                    n.nodes[index] = node(s[0])
                n = n.nodes[index]
            if i == len(s) -1:
                # the last one
                n.health = 1
                return
            index = self.indexes[s[i+1]]
            if not n.nodes[index]:
                n.nodes[index] = node(s[:i+2])
            self.insert(s, i + 1, n.nodes[index])

    def search(self, s):
        return self.search2(s, 0, self.root)

    def search2(self, s, start, n):
        if start >= len(s):
            return True
        index = self.indexes[s[start]]
        if n.nodes[index]:
            return self.search2(s, start+1, n.nodes[index])
        else:
            return False

    def printTree(self, node = None):
        if not node:
            node = self.root
        queue = [node]
        while len(queue) > 0:
            t = queue.pop(0)
            if t:
                print(t.val, end = ' ')
                print(f'id is {t.health}', end = ' ')
                print(t.fail.val if t.fail else 'NUL', end = ' ')
                print(t.end.val if t.end else 'NUL', end = ' ')
                queue.extend(t.nodes)
                print(len(queue))

    def search_text(self, text):
        start = 0
        n = self.root
        while start < len(text):
            index = self.indexes[text[start]]
            while True:
                if n.nodes[index]:
                    n = n.nodes[index]
                    break
                if n == self.root:
                    break
                n = n.fail
            # calcuate matches.
            m = n
            while True:
                if m and m.health > 0:
                    print(f'found {m.val} at {start + 1 - len(m.val)}')
                if m == self.root:
                    break
                m = m.end
            start += 1


if __name__  == '__main__':
    s = ['abcde', 'abdefe', 'bcd', 'c']
    t = trie()
    t.build_tree(s)
    t.printTree(t.root)
    text= 'cccccc'
    text = 'bcdeabcdeabcdefeabdefeccccbcdec'
    print(text)
    t.search_text(text)
    #print(t.search('abd'))
    #print(t.search('abcde'))
    #print(t.search('abb'))

