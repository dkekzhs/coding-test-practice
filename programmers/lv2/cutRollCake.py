from functools import reduce
from collections import Counter
def solution(topping):
    answer = 0
    a = set()
    dic = Counter(topping)
    print(dic)
    for i in topping:
        dic[i] -= 1
        a.add(i)
        if dic[i] == 0 :
            dic.pop(i)
        if len(dic) == len(a):
            answer+=1
  

    return answer

solution([1, 2, 1, 3, 1, 4, 1, 2])