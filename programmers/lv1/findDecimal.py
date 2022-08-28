import math
def sosu(x):
    if x == 2 : 
        return True
    elif x== 1 : 
        return False
    for i in range(2,int(math.sqrt(x) +1)):
        if x%i == 0:
            return False
    return True
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if sosu(i) == True:
            answer+=1
    return answer
solution(10)