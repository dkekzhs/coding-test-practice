import math
import time

start = time.time()
def fibo(x):
    if x == 1 or x== 2:
        return 1
    return fibo(x-1) + fibo(x-2)
fibo(35)
end = time.time()

print(f"{end - start:.5f} sec")

start = time.time()
d = [0] * 100

def fibo(x):
    if x==1 or x==2:
        return 1
    if d[x] != 0 :
        return d[x]
    else:
        d[x] = fibo(x-1) + fibo(x-2)
    
end = time.time()

print(f"{end - start:.5f} sec")

