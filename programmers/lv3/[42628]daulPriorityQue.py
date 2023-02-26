from collections import deque
def solution(operations):
    answer = []
    deq = deque()
    for oper in operations:
        temp = oper.split()
        if temp[0] == "I":
            if deq:
                if deq[0] > int(temp[1]):
                    deq.appendleft(int(temp[1]))
                else:
                    deq.append(int(temp[1]))
            else:
                deq.append(int(temp[1]))
        elif temp[0] == "D" and temp[1] == "-1":
            if deq:
                deq.popleft()
            else:
                continue
        elif temp[0] == "D" and temp[1] == "1":
            if deq:
                deq.pop()
            else:
                continue
    if deq:
        answer = [max(deq),min(deq)]
    else:
        answer = [0,0]
    return answer
