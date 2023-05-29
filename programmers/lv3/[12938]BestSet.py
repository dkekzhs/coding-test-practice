def solution(n, s):
    answer = []
    if n== 1:
        return s
    if s// n == 0:
        return [-1]
    while n :
        answer.append(s//n)
        s-= s//n
        n-=1
    return answer


solution(3,9)