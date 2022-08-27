def solution(a, b):
    answer = 0
    pre = 0
    if a> b:
        pre = a
        a = b
        b= pre
    for i in range(a,b+1):
        answer += i
    
    return a if a==b else answer
