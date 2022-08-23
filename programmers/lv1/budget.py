
def solution(d, budget):
    answer = 0
    a = []
    d.sort()
    for i in d:
        budget += -i
        if budget < 0:        
            a.append(i)
    
    answer =len(d) - len(a)    
    return answer
