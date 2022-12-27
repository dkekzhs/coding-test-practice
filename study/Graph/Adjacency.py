import math

# 서로 연결되어 있지 않은 노드 초기화 하는법
INF = 999999
INF = math.inf

graph = [[0,5,10],
         [5,0,INF],
         [10,INF,0]]
print(graph)

graph = [[] for _ in range(3)]

#노드 A에 연결된 노드 정보
graph[0].append(("B",5))
graph[0].append(("C",10))

#노드 B에 연결된 노드 정보
graph[1].append(("A",5))

#노드 C에 연결된 노드 정보
graph[2].append(("A",10))

print(graph)