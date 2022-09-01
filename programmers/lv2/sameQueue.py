from collections import deque
def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    left_val = sum(queue1)
    right_val = sum(queue2)
    for x in range(len(queue1) *3):
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


solution([1,1],[1,2])