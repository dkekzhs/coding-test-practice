def util1(m,n):
    count = 0
    while True:
        if m == 1 :
            break
        if m % n == 0 :
             m = m // n 
             count += 1
        else : 
            m -= 1
            count +=1 

    print(count)

def util2(n,k):
    result = 0
    while True:
        target = (n//k) * k
        result +=  n - target
        n = target

        if n < k:
            break
        result +=1 
        n //= k

    result += (n-1)

util2(25,3)