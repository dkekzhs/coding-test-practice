import math
import heapq
n,m,start = 3,2,1
data = [[1,2,4],[1,3,2]]

graph = [[]for _ in range(n+1)]
print(graph)
distance = [math.inf for _ in range(n+1)]

for a,b,c in data:
    graph[a].append((b,c))

def dj(start):
    h = []
    heapq.heappush(h,(0,start))
    distance[start] = 0
    while h:
        dist, now = heapq.heappop(h)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(h,(cost,i[0]))
dj(start)
count = 0
max_dis = 0
for d in distance:
    if d != math.inf:
        count+=1
        max_dis = max(max_dis,d)
print(count -1 , max_dis)