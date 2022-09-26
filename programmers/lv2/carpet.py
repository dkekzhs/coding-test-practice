import math

def solution(brown, yellow):
    answer = []
    
    all = brown + yellow
    for i in range(1,all+1):
        if all%i == 0:
            for j in range(i,all):
                if all%j == 0:
                    if i-2 <0 and j-2<0:
                        pass
                    elif (i-2)*(j-2) == yellow:
                        answer.append(j)
                        answer.append(i)
                        return answer

    return answer
