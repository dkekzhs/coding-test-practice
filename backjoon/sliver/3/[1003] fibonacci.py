import sys

n = int(sys.stdin.readline())
for i in range(n):
    j = int(sys.stdin.readline())
    cnt0 = [1,0]
    cnt1 = [0,1]
    for x in range(2,j+1):
        cnt0.append(cnt0[x-1]+cnt0[x-2])
        cnt1.append(cnt1[x-1]+cnt1[x-2])
    print(cnt0[j],cnt1[j])