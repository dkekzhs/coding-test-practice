n,m = map(int,input().split())
data = []
for i in range(n):
    data.append(input())
k = int(input())
answer = 0

for i in range(n):
    zeroCount = 0
    for j in data[i]:
        if j == "0":
            zeroCount +=1

    lightCount = 0
    if zeroCount <=k and zeroCount%2 == k%2:
        for i2 in range(n):
            if data[i] == data[i2]:
                lightCount+=1
    answer = max(answer,lightCount)


print(answer)