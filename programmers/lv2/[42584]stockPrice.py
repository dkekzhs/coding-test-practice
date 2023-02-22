from collections import deque
def solution(prices):
    answer =[]
    que = deque(prices)
    while que:
        price = que.popleft()
        cnt = 0 
        for c in que:
            cnt +=1 
            if price> c:
                break
        answer.append(cnt)
    print(answer)
    return answer
solution([1, 2, 3, 2, 3])