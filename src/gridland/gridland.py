
def gridlandProvinces(s1, s2):
    # Write your code here
    total = len(s1) + len(s2)
    visited = [[0]*len(s1), [0]*len(s2)]
    s = [s1, s2]
    labels = []
    cur = (0, 0)
    visited[0][0] = 1
    labels.append((0,0))
    directions = [0] * (total -1)
    #going next.
    results = set()
    i = 0
    while True:
        if i == len(directions):
            # got one
            # print(labels)
            val = []
            for ll in labels:
                val.append(s[ll[0]][ll[1]])
            results.add(''.join(val))
            i -= 1
            if i == 0:
                break
            visited[cur[0]][cur[1]] = 0
            labels.pop()
            cur = labels[-1]
            directions[i] += 1
        #print(i, directions, visited, labels, '-', cur)
        if directions[i] == 0:
            if cur[0] > 0 and visited[cur[0]-1][cur[1]] == 0:
                cur = (cur[0]-1, cur[1])
                visited[cur[0]][cur[1]] = 1
                labels.append(cur)
                i+=1
            else:
                directions[i] += 1
        elif directions[i] == 1:
            if cur[0] == 0 and visited[cur[0]+1][cur[1]] == 0:
                cur = (cur[0]+1, cur[1])
                visited[cur[0]][cur[1]] = 1
                labels.append(cur)
                i+=1
            else:
                directions[i] += 1
        elif directions[i] == 2:
            if cur[1] > 0 and visited[cur[0]][cur[1]-1] == 0:
                cur = (cur[0], cur[1] -1)
                visited[cur[0]][cur[1]] = 1
                labels.append(cur)
                i+=1
            else:
                directions[i] += 1
        elif directions[i] == 3:
            if cur[1] < len(s1)-1 and visited[cur[0]][cur[1]+1] == 0:
                cur = (cur[0], cur[1] + 1)
                visited[cur[0]][cur[1]] = 1
                labels.append(cur)
                i+=1
            else:
                directions[i] += 1
        elif directions[i] == 4:
            # backtrack.
            for j in range(i, len(directions)):
                directions[j] = 0
            if i == 0:
                break
            visited[cur[0]][cur[1]] = 0
            labels.pop()
            cur = labels[-1]
            directions[i-1] += 1
            i -= 1
    print(results)


gridlandProvinces('dab', 'abd')
