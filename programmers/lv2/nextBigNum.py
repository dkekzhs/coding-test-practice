def solution(n):
    a = bin(n)[2:]
    b= n
    acount = a.count("1")
    print(a,)
    while True:
        b+=1
        c= bin(b)[2:]
        if acount == c.count("1"):
            return b

solution(78)