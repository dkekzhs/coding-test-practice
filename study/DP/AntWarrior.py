a = [1,3,1,5]

d= [0] * 100

d[0] = a[0]
d[1] = max(a[0],a[1])
for i in range(2,len(a)):
    d[i] = max(d[i-1],d[i-2]+a[i])
print(d)
print(d[len(a)-1])