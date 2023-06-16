def solution(land):
    answer = 0
    dp = [[0 ] * 4 for _ in range(len(land) )]
    
    for i in range(len(land)):
        for j in range(len(land[i])):
            for k in range(len(land[i])) :
                if j == k :
                    continue
                dp[i][j] = max(dp[i][j], dp[i-1][k] + land[i][j])

    answer = max(dp[len(dp)-1])

    return answer 

solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]])