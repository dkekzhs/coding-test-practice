def solution(n):
    answer = ''
    a = 0
    for i in range(0,n):
        if a==0:
            answer+= "수"
            a=1
        else:
            a= 0
            answer +="박"
    return answer

solution(3)