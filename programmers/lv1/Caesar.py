def solution(s, n):
    answer = ''
    b=0
    for i in s:
        if ord(i) >= 65 and ord(i) <= 90: #대문자일때
            if ord(i) + n> 90 :
                b = abs(-(90 - ord(i)) + n)
                answer += chr(64 + b)
            else:
                answer+=chr(ord(i)+n)
        elif ord(i) >= 97 and ord(i) <=122: #소문자일때
            if ord(i) + n> 122 :
                b = abs(-(122 - ord(i)) + n)
                
                answer += chr(96 + b)
            else:
                answer+=chr(ord(i)+n)
        else :
            answer+= " "

    return answer
