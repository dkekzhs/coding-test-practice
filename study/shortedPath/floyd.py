import math
n,m = 4,7
graph = [[math.inf for _ in range(n+1)] for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a== b :
            graph[a][b] = 0

inputG = [[1,2,4],
        [1,4,6],
        [2,1,3],
        [2,3,7],
        [3,1,5],
        [3,4,4],
        [4,3,2]]

for a,b,c in inputG:
        graph[a][b] = c

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b] == math.inf:
            print("INF")
        else:
            print(graph[a][b], end=" ")
    print()