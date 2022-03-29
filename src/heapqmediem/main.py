import heapq
def findMedian(arr):
    # Write your code here
    left = []
    right = []
    lefttop = -1
    righttop = -1
    for a in arr:
        print(left, right, lefttop, righttop)
        if lefttop == -1:
            lefttop = a
            continue
        if righttop == -1:
            if a <= lefttop:
                righttop = lefttop
                lefttop = -heapq.heappushpop(left, -a)
            else:
                righttop = heapq.heappushpop(right, a)
        else:
            if a <= lefttop:
                heapq.heappush(a)
                heapq.heappush(righttop)
                righttop = -1
            elif a <= righttop:
                heapq.heappush(left, -lefttop)
                heapq.heappush(right, righttop)
                lefttop = a
                righttop = -1
            else:
                heapq.heappush(left, -lefttop)
                heapq.heappush(right, a)
                lefttop = righttop
                righttop = -1
    return lefttop

if __name__ == '__main__':
    arr =  [0,1,5,2,4,6, 7,3]
    result = findMedian(arr)
    print(result)


