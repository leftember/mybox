def equal(arr):
    m = min(arr)
    t = [0]*3
    for i in arr:
        for j in range(3):
            x = i-(m-j)
            x = x//5 +(x%5)//2 + (x%5)%2 
            t[j]+=x
            print(m, i, j, x, t)
    return min(t)

for _ in range(int(input())):
    arr = list(map(int,input().split()))
    arr = sorted(arr)
    print(equal(arr))
