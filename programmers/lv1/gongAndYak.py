
def solution(n, m):
    a = n
    b =m
    tmp =0
    if m < n:
        tmp = m
        m= n
        n = tmp
    while m%n :
        r = m%n
        m = n
        n = r


    return [n,a*b/n]
    
solution(2,5)
