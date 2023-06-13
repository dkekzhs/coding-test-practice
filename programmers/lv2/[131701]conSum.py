from itertools import combinations 
def solution(elements):
    a =set()
    N = len(elements)
    elements = elements * 10
    for i in range(N+1):
        k = 0
        while k < N:
            ad = sum(elements[k:k+i])
            k+=1
            a.add(ad)


    

    return len(a)-1


solution([7,9,1,1,4])