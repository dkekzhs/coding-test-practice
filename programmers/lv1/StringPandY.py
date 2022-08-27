def solution(s):
    cnt = 0
    s =s.lower()
    for i in s:
        if i == "p":
            cnt+= 1
        elif i == "y":
            cnt-= 1
    return True if cnt ==0 else False

solution("pPoooyY")