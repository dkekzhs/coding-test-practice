import re
def solution(s):
    answer = []
    dic={}
    
    a = re.findall("\d+",s)
    for i in a:
        if  i not in dic:
            dic[i] = a.count(i)

    while len(dic) !=0:
        for k,v in dic.items():
            if max(dic.values()) == v :
                answer.append(int(k))
                dic.pop(k)
                break

            
    return answer



solution("{{20,111},{111}}")