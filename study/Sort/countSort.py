a = [1,3,2,4,5,0]

count = [0] * (max(a)+1)
for i in range(len(a)):
    count[a[i]] +=1

for i in range(len(count)):
    for j in range(count[i]):
        print(i,end='')