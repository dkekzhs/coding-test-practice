import re
def prime(number):
    if number==1:
        return False
    for i in range(2,int(number**(0.5))+1):
        if number%i==0:
            return False
    return True
def demical(n,k):
    cz=""
    while n :
        cz += str(n%k)
        n = n//k
        
    return cz[::-1]


def solution(n, k):
    answer = 0
    a = demical(n,k)
 
    #0P0 , P0 , 0P, P , P는 0을 포함하지 않습니다.
    c = a.split("0")
    spl = [int(i) for i in c if i!=""]
    for i in spl:
        if prime(i):
            answer+=1

    return answer


