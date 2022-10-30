def solution(fees, records):
    answer = []

    dic = {}
    dic2 = {}
    for i in records:
        b = i.split( )
        if b[1] not in dic:
            dic[b[1]] = [b[0]] 
        elif b[1] in dic and b[2] !="OUT":
            dic[b[1]] += [b[0]]
        
    for j in records:
        c = j.split( )  
        if c[1] not in dic2 and c[2] == "OUT":
            dic2[c[1]] = [c[0]]
        elif c[1] in dic2 and c[2] != "IN":
            dic2[c[1]] += [c[0]]
    dic3 ={}
    for k,v in dic.items():
        if dic2.get(k) == None:
            dic2[k] =["23:59"]
        if k in dic2.keys():
            out = dic2.get(k)
            
            if len(v) != len(out):
                dic2[k] += ["23:59"]
            for a,s in zip(out,v): # a는 출차 s는 입차
                out_si,out_bun = a.split(":") 
                in_si,in_bun = s.split(":")
                total = (int(out_si) - int(in_si)) * 60 + (int(out_bun)- int(in_bun))
                if k not in dic3:
                    dic3[k] = total
                else:
                    dic3[k] += total
 
    sorted_dict = sorted(dic3.items())
    for z,x in sorted_dict:
        if x <= fees[0]:
            answer.append(fees[1])
        else:
            b = x - fees[0]
            gak = fees[1]
            while b >0: 
                b -= fees[2]
                gak += fees[3]
            answer.append(gak)

    return answer

print(solution([1, 461, 1, 10],["00:00 1234 IN"]))