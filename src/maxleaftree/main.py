from collections import deque

class node:
    def __init__(self, val):
        self.v = val
        self.left = None
        self.right = None

    def print_subtree(self):
        result = []
        todo = deque([(self, 32)])
        indent = [' '] * 2
        while len(todo) > 0:
            nexttodo = deque()
            newline = []
            result.append(newline)
            while len(todo) > 0:
                t = todo.popleft()
                newline.append((t[0].v,t[1]))
                delta = (t[1]&-t[1]) // 2
                if t[0].left:
                    nexttodo.append((t[0].left, t[1]-delta ))
                if t[0].right:
                    nexttodo.append((t[0].right, t[1] + delta))
            todo = nexttodo

        for r in result:
            # print(' '.join(r))
            for i in range(len(r)):
                leadingspaces = r[i][1] - r[i-1][1]-len(str(r[i][0])) if i > 0 else r[i][1]
                print(' '* leadingspaces, r[i][0], end = '')
            print('')

def calreachtree(root):
    if root.left and not root.right:
        root.v += calreachtree(root.left)
    elif root.right and not root.left:
        root.v += calreachtree(root.right)
    elif root.left and root.right:
        root.v += max(calreachtree(root.left), calreachtree(root.right))
    return root.v

def findmaxintree(root):
    summax = 0
    if root.left and root.right:
        cur = root.v + min(root.left.v, root.right.v)
        if cur > summax:
            summax = cur
    if root.left:
        summax = max(summax, findmaxintree(root.left))
    if root.right:
        summax = max(summax, findmaxintree(root.right))
    return summax


def calcmaxsum(root):
    calreachtree(root)
    root.print_subtree()
    return findmaxintree(root)



if __name__ == '__main__':
    root = node(1)
    root.left = node(2)
    root.right = node(3)
    t = root.right
    t.right = node(6)
    t.left = node(2)
    t = t.left
    t.left = node(10)
    t.right = node(1)
    root.print_subtree()
    rr = calcmaxsum(root)
    print('max sum is', rr)

