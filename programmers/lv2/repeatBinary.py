def binary(s) :
    rev_base =""
    while s>0 :
        s,v = divmod(s,2)
        rev_base += str(v)
    return rev_base[::-1]

def solution(s):
    answer = []
    count = 0
    cnt0 = 0
    while s != "1":
        count += 1
        cnt0 += s.count("0")
        s = s.replace("0","")
        s = binary(len(s))
        
    answer.append(count)
    answer.append(cnt0)

    return answer

solution("110010101001")