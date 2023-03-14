def solution(k, tangerine):
    answer = 0
    dic = {}
    for i in tangerine:
        if i in dic.keys():
            dic[i] +=1
        else:
            dic[i] = 1
    dic2 = sorted(dic.items() , key=lambda x :x[1],reverse=True)
    for name,siz in dic2:
        if k > 0:
            break
        else:
            k -= siz
            answer+=1
    
    return answer

solution(6,[1, 3, 2, 5, 4, 5, 2, 3])