from collections import deque
def solution(s):
    answer = 0
    n = len(s)
    
    for i in range(n):
        a = s[:i]
        b = s[i:]
        c = b+a 
        check = check_data(c)
        if check :
            answer +=1 
    return answer            
def check_data(s):
    a = deque(s)
    if a[0] == "}" or a[0] == ")" or a[0] == "]":
        return False
    closes = {"}":"{", "]":"[", ")":"("}
    dq = deque()    
    for char in a:
        if dq and char in closes and closes[char] == dq[-1]:
            dq.pop()
        elif char in closes:
            return False
        else:
            dq.append(char)
    
    return len(dq) == 0
    
    
solution("{(})")