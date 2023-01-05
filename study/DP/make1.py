x= 26

d = [0] * 100

for i in range(1,x+1):
    d[i] = d[i-1] + 1
    if d[i] % 2 == 0:
        d[i] = min(d[i],d[i//2]+1)
    elif d[i] % 3 == 0 :
        d[i] = min(d[i],d[i//4]+1)
    elif d[i] % 5 == 0 :
        d[i] = min(d[i],d[i//5]+1)
print(d[x])
