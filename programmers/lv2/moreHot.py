import heapq

def solution(sv, K):
    answer = 0
    heapq.heapify(sv)
    
    while sv[0] < K :
        heapq.heappush(sv,heapq.heappop(sv) + heapq.heappop(sv) *2) 
        answer+=1
        
        if len(sv) == 1 and sv[0] < K:
            return -1

    return answer
