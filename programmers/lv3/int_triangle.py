def solution(triangle):
    answer = triangle[0][0]
    if len(triangle) == 2:
        answer += max(triangle[1])
    else:
        l = len(triangle)
        dp = [0] * l
        dp[0] = triangle[0]
        for i in range(1,len(triangle)):
            dp[i] = [0] * (i+1)
            for j in range(i+1):
                if j == 0 :
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j==i:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else:
                    dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + triangle[i][j]
        answer = max(dp[l-1])

    return answer
solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])