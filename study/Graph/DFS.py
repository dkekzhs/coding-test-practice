def dfs(graph,v,visit):
    visit[v] = True
    print(v, end="")
    for i in graph[v]:
        if not visit[i]:
            dfs(graph,i,visit)

graph = [[],[2,4,7],
            [1,6,8],
            [4,5],
            [1,3,5],
            [3,4],
            [2,7],
            [1,6],
            [2]]


visit = [False] * 9

dfs(graph,1,visit)