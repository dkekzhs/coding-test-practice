from collections import deque

def bfs(graph,start,visit):
    queue = deque([start])
    visit[start] = True
    while queue:
        v= queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visit[i]:
                queue.append(i)
                visit[i] = True




graph = [[],[2,4,7],
            [1,6,8],
            [4,5],
            [1,3,5],
            [3,4],
            [2,7],
            [1,6],
            [2]]


visit = [False] * 9

bfs(graph,1,visit)