import math
import heapq


def dj(start,graph,distance):
    q =[]
    heapq.heappush(q,(0,start))
    distance[start] = 0 
    while q:
        dist, now = heapq.heappop(q) 
        if distance[now] < dist:
            continue
        for i in graph[now]:  
            cost = dist + i[1]
            if cost < distance[i[0]]: 
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0])) 


def solution(N, road, K):
    answer = 0
    graph =[[] for _ in range(N+1)]
    for a,b,c in road:
        graph[a].append((b,c))
        graph[b].append((a,c))
    
    distance = [math.inf] * (N+1)
    dj(1,graph,distance)
    for d in distance:
        if d<= K:
            answer+=1

    return answer

solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3)