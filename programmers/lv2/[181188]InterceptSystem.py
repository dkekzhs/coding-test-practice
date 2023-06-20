def solution(targets):
    answer= 0 
    shoot = -1 
    targets.sort(key = lambda x : x[1])
    for target in targets :  
        if target[0] > shoot:
            answer+=1
            shoot = target[1] - 0.0005
    
    return answer

