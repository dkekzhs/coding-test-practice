import math
import heapq
N,M = 6, 11
start = 1
inputG = [[1,2,2],
        [1,3,5],
        [1,4,1],
        [2,3,3],
        [2,4,2],
        [3,2,3],
        [3,6,5],
        [4,3,3],
        [4,5,1],
        [5,3,1],
        [5,6,2]]
graph = [[] for _ in range(N+1)]
for a,b,c in inputG:
    graph[a].append((b,c))

distance = [math.inf] * (N+1)

def dijkstra(start):
    q = []
    
	#시작 노드로 가기위한 최단경로는 0으로 설정하고 (우선순위)큐에 삽입
    heapq.heappush(q,(0, start)) 
    distance[start] = 0

	# 큐가 비어있지 않다면
    while q:
        dist, now = heapq.heappop(q) # 거리가 가장 짧은 노드를 큐에서 꺼냄
        # 현재 노드가 이미 처리된적 있는 노드라면 무시
        # 현재 꺼낸 그 원소의 거리값(dist)이 테이블에 기록되어있는 값 보다 더 크다면 이미 처리된 것
        if distance[now] < dist:
            continue
        # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
        for i in graph[now]: # 현재 노드와 연결된 다른 인접 노드 
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]: #현재 노드를 거쳐가는 것과 기존의 값을 비교
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0])) # (거리, 노드)

                

dijkstra(start)

for i in range(1, N+1):
    if distance[i] == math.inf:
        print('inf')
    else:
        print(distance[i])