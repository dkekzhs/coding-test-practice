def solution(n):
    b = []
    for i in (range(1,n)):
        if n%i == 1:
            b.append(i)
        else:
            pass
    return min(b)

solution(10)