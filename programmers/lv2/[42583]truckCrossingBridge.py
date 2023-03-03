## 다리 길이 만큼 시간이 걸린다.
from collections import deque
def solution(bridge_length, weight, truck_weights):
    deq = deque(truck_weights)
    answer=0

    corssing = deque([])

    while True:
        weight_sum = 0

        if not deq:
            if not corssing:
                break
        answer+=1

        if corssing:
            if corssing[0][1] >= bridge_length:
                corssing.popleft()
        if corssing:
            for i in range(len(corssing)):
                corssing[i][1] +=1
        if corssing:
            for i in range(len(corssing)):
                weight_sum += corssing[i][0]
        if deq:
            if len(corssing)+1 <= bridge_length and (weight_sum+deq[0]) <=weight:
                temp = deq.popleft()
                corssing.append([temp,1])
    
            

    return answer

solution(2,10,[7,4,5,6])
solution(100,100,[10])
solution(100,100,[10,10,10,10,10,10,10,10,10,10])