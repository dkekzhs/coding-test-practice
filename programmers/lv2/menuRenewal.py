import itertools 
def solution(orders, course):
    answer = []
    c = {}
    val= []
    val2 =[]
    for i in course:
        for j in orders:
            if len(j) >= i:
                z = itertools.combinations(j,i)
                for b in z:
                    b= sorted(b,reverse=False)
                    if "".join(b) not in c:
                        c["".join(b)] = 1
                    else : 
                        c["".join(b)] += 1
    for j in course:
        val.clear()
        val2.clear()
        for k,v in c.items():
            if len(k) == j and v >=2 :
                val.append(k)
                val2.append(v)
        for q,w in zip(val,val2):
            maxz =max(val2)
            if maxz == w :
                answer.append(q)
    return sorted(answer , reverse=False)
