def sam(x):
    a = list(str(x))
    count = 0
    for i in range(len(a)):
        if a[i] == "3" or a[i] == "6" or a[i] == "9":
            count+=1
    if count == 0 :
        return x
    else:
        return "-"*count


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
N = int(input())
for i in range(1,N+1):
    s = sam(i)
    print(str(s), end=" ")