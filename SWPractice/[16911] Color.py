from collections import deque
T = int(input())
def Test(N,A): 
    dp = [0] * (N+1)
    dp[1] = A[0]
    dp[2] = A[1]
    for i in range(3,N+1):
        dp[i-1] = max(dp[i-1],A[i-1])
        dp[i-2] = max(dp[i-2],A[i-2])
        dp[i] = min(dp[i-1] + dp[i-2], dp[i-2]+A[i-2], dp[i-1]+A[i-2])
    return dp[N]

                








# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    A = list(map(int,input().split()))
    
    total_cost = Test(N,A)
    print("#"+str(test_case)+" "+str(total_cost))

