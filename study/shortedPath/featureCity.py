import math
n,m = 5,7
b = [[1,2],
    [1,3],
    [1,4],
    [2,4],
    [3,4],
    [3,5],
    [4,5]]
x, k =4,5

graph = [[math.inf for _ in range(n+1)] for _ in range(n+1)]
for a in range(1,n+1):
    for c in range(1,n+1):  
        if a==c:
            graph[a][c] = 0
for a,c in b:
    graph[a][c] =1
    graph[c][a] =1

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

distance = graph[1][k] + graph[k][x]
if distance >= math.inf:
    print(-1)
else:
    print(distance)