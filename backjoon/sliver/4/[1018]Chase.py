n,m = map(int,input().split( ))
arr = []
answer=[]
for i in range(n):
    arr.append(list(input()))

for i in range(n-7):
    for j in range(m-7):
        d1,d2 = 0,0
        for a in range(i,i+8):
            for b in range(j,j+8):
                if (a + b) % 2 == 0:
                    if arr[a][b] != 'B':
                        d1 += 1
                    if arr[a][b] != 'W':
                        d2 += 1
                else:
                    if arr[a][b] != 'W':
                        d1 += 1
                    if arr[a][b] != 'B':
                        d2 += 1
 
        answer.append(d1)
        answer.append(d2)
print(min(answer))