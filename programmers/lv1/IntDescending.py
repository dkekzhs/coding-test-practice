def solution(n):
    b= []
    for i in str(n):
        b.append(i)

    return int("".join(sorted(b,reverse=True)))

solution(118372)