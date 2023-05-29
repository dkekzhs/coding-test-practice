import heapq
def solution(n,works):
    answer = 0
    if sum(works) < n:
        return answer
    works = [(-1) * work for work in works]
    heapq.heapify(works)
    for _ in range(n):
        cur = heapq.heappop(works)
        nxt = cur +1
        heapq.heappush(works,nxt)

    for i in range(len(works)):
        answer +=works[i] ** 2
    
    return answer

print(solution(4,[4, 3, 3]))