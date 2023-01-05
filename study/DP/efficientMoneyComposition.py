import math
N,M = 2,15
change = [2,3]
d = [math.inf]  * (M+1)

d[0] = 0

for i in range(N):
    for j in range(change[i],M+1):
        if d[j -change[i]] != math.inf:
            d[j] = min(d[j],d[j- change[i]] + 1)

print(d)
if d[M] == math.inf:
    print(-1)
else:
    print(d[M])
