def solution(cacheSize, cities):
    answer = 0
    cnt = 0 
    dic = {}
    cities2= []
    if cacheSize == 0 :
        return 5* len(cities)
    for i in cities:
        cities2.append(i.lower())

    for i in cities2:
        cnt+=1
        if i not in dic and len(dic) < cacheSize:
            answer += 5
            dic[i] = cnt
        else:
            if i in dic :
                answer+=1
                dic[i] = cnt
            else:
                
                for k ,v in dic.items():
                    if v == min(dic.values()):
                        dic.pop(k)
                        answer+=5   
                        dic[i] = cnt     
                        break
                


    return answer

solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])