def solution(routes):
    rout = sorted(routes,key=lambda x : x[0])
    answer = 1
    m = 30000
    for i,j in rout:
        if i>m:
            answer +=1 
            m= j 
        m = min(i,j)
    

    return answer

solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])