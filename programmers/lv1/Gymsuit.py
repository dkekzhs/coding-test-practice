def solution(n, lost, reserve):
    dic ={}
    answer = 0    
    for i in range(1,n+1):
        dic[i] = 1
        if i in lost:
            dic[i] += -1 
        if i in reserve:
            dic[i] +=1 
    for i in dic:
        if i==1:
            if dic[i + 1] >1 and dic[i] ==0:
                dic[i+1] += -1
                dic[i] += 1
        elif i ==len(dic):
            if dic[i-1] >1 and dic[i] == 0:
                dic[i-1] += -1
                dic[i] += 1
        elif dic[i - 1] > 1 and dic[i] == 0:
            dic[i - 1] += -1
            dic[i ] += 1                
        elif dic[i + 1] >1 and dic[i] ==0:
            dic[i + 1] += -1
            dic[i] += 1 



    for i in dic :
        if dic[i] > 0:
            answer+=1
    print(dic)
    print(answer)

    return answer
solution(5, [2, 4], [3, 5])