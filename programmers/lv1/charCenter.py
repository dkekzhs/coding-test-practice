def solution(s):
    v = int(len(s)/2)    
    if len(s)%2 == 0:
        return s[v-1:v+1]
    else: 
        return s[v]


solution("qwer")