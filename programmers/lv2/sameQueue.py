from collections import deque
def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    left_val = sum(queue1)
    right_val = sum(queue2)
    while range(len(queue1)):
        if left_val > right_val:
            left_val -= queue1[0]
            right_val += queue1[0]
            queue2.append(queue1.popleft())
        elif right_val> left_val:
            left_val += queue2[0]
            right_val -= queue2[0]
            queue1.append(queue2.popleft())
        else:
            return answer
        answer +=1


    return -1


solution([3,2,7,2],[4,6,5,1])