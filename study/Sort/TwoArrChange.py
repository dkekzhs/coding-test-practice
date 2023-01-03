n,k =5,3
a = [1,2,5,4,3]
b = [5,5,6,6,5]

for i in range(k):
    a_min = min(a)
    a_idx = a.index(a_min)
    b_min =  max(b)
    b_idx = b.index(b_min)
    a[a_idx],b[b_idx] = b[b_idx],a[a_idx]

print(sum(a))

n,k =5,3
a = [1,2,5,4,3]
b = [5,5,6,6,5]

a.sort()
b.sort(reverse=True)
for i in range(k):
    if a[i] < b[i]:
        a[i] ,b[i] = b[i],a[i]
    else:
        break
print(sum(a))
