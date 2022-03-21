"""
TriE tree for string search
"""


class node:
     def __init__(self, v):
         self.val = v
         self.nodes = [None] * 26
         self.fail = None

class trie:
    indexes = {}
    def __init__(self):
        self.root = node(None)
        #self.indexes = 'aaa' #instance variable can block static variable if present.
        if len(trie.indexes) == 0:
            # initialize
            for i in range(26):
                trie.indexes[chr(ord('a')+i)] = i

    def insert(self, s, i = 0, n = None):
        if i < len(s):
            if (i == len(s) -1):
                # the last one
                return
            if not n: # root node
                n = self.root
                index = self.indexes[s[0]]
                if not n.nodes[index]:
                    n.nodes[index] = node(None)
                n = n.nodes[index]
            index = self.indexes[s[i+1]]
            if not n.nodes[index]:
                n.nodes[index] = node(None)
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
                print(f'id is {id(t)}', end = ' ')
                queue.extend(t.nodes)
                print(len(queue))

if __name__  == '__main__':
    s = 'abcde'
    t = trie()
    t.insert('abcdfe')
    t.insert(s)
    t.printTree(t.root)
    print(t.search('abd'))
    print(t.search('abcde'))
    print(t.search('abb'))

