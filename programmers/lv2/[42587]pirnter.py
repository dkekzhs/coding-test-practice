from collections import deque
def solution(priorities, location):
    t = [(priorities[i], i) for i in range(len(priorities))]
    a = deque(t)
    temp = []
    while a :
        data = a.popleft()
        flag = 0
        for i in a:
            if data[0] < i[0]:
                a.append(data)
                flag =1
                break
        if flag == 0 :
            temp.append(data)
    answer = 0
    for i in range(len(priorities)):
        if temp[i][1] == location:
            answer = i+1
            break
    
    return answer

solution([1, 1, 9, 1, 1, 1],0)