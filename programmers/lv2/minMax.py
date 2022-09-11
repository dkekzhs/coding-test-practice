def solution(s):
    answer =""
    a = s.split(" ")
    b = []
    for i in a:
        b.append(int(i))
    b = sorted(b)
    answer = str(b[0]) + " " + str(b[len(b)-1])
        
        
    return answer
solution("-1 -2 -3 -4")
