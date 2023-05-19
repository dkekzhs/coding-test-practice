from collections import deque
import itertools 

def Hex(a):
    tt = ''.join(s for s in a)
    return int(tt,16)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,K = map(int,input().split())
    inP = input()
    data = deque(inP)
    Z  = N//4
    arr = []
    arr2 = []
    for i in range(0,N,Z):
        a = list(itertools.islice(data,i,i+Z))
        arr.append(Hex(a))
    c= 0
    ff = len(arr)
    while c != ff:
        c = 0
        data.rotate(1)
        for i in range(len(arr)):
            if arr[i] in arr2:
                c +=1 
        if c == ff:
            break
        for i in range(0,N,Z):
            a = list(itertools.islice(data,i,i+Z))
            arr2.append(Hex(a))
    arr2.sort(reverse=True)
    top = set(arr2)
    top = list(top)
    top.sort(reverse=True)
    print("#"+str(test_case)+" "+ str(top[K-1]))


# 1
# 12 10
# 1B3B3B81F75E
# 16 2
# F53586D76286B2D8
# 20 14
# 88F611AE414A751A767B
# 24 16
# 044D3EBA6A647B2567A91D0E
# 28 11
# 8E0B7DD258D4122317E3ADBFEA99