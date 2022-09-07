def solution(x, n):
    answer = []
    count = n
    anw = x
    while count != 0 :
        answer.append(anw)
        anw += x
        count-=1 
    print(answer)
    return answer

solution(2,5)