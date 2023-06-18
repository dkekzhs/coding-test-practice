import math
def solution(n, stations, w):
    answer = 0
    idx = 1
    for station in stations:
        l,r = station - w , station + w 
        if l < 1 :
            l = 1
        if r > n :
            r = n
        answer += math.ceil((l- idx)/(2*w+1))
        idx = r +1

    if n - idx >= 0 :
        answer += math.ceil((n-idx+1)/(2*w+1))
        
    
    

    return answer

solution(11,[4, 11],1)