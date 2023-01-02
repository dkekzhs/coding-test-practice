a = [1,3,2,4,5,0]

for i in range(len(a)):
    min_idx = i
    for j in range(i+1,len(a)):
        if a[min_idx] > a[j]:
            min_idx = j
        a[i],a[min_idx] = a[min_idx],a[i]
print(a)