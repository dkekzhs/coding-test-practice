T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    M = N
    a = [[0 for _ in range(N)] for _ in range(N)]
    row, col = -1,0
    cnt =1 
    trans = 1
    while N>0:
        for i in range(N):
            row +=trans 
            a[row][col] = cnt
            cnt+=1
        N -=1 
        for j in range(N):
            col += trans
            a[row][col] = cnt
            cnt+=1
        trans *=-1
    j = 0
    print("#"+str(test_case))
    while j != len(a[0]):
        for i in range(M):
            print(a[i][j],end=' ')
        print()
        j+=1


# 2    
# 3   
# 4      