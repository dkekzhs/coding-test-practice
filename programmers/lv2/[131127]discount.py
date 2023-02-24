def solution(want, number, discount):
    answer = 0
    n = len(discount)
    for i in want:
        if i not in discount:
            return 0
    data = {}
    data2= {}
    for i in range(len(want)):
        data[want[i]] = number[i]
    for i in range(n):
        if data == data2:
            answer+=1 
        if i+10 >n:
            break
        data2= {}
        for j in range(i,i+10):
            if discount[j] not in data2:
                data2[discount[j]] = 1
            else:
                data2[discount[j]] +=1
    return answer


solution(["banana", "apple", "rice", "pork", "pot"],[3, 2, 2, 2, 1],["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"])