def solution(n):
    answer = []
    n = str(n)
    i=len(n)
    while i !=0 :
        answer.append(int(n[i-1]))
        i+= -1
    print(answer)
    return answer

solution(13245)