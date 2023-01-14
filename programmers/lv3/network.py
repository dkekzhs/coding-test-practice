
def solution(n, computers):
    answer = 0
    visit = [False] * n
    for i in range(n):
        if visit[i] == False:
            dfs(i,visit,n,computers)
            answer+=1

    return answer


def dfs(i,visit,n,computers):
    visit[i] =True
    for j in range(n):
        if i != j and computers[i][j]== 1:
            if visit[j] == False:
                dfs(j,visit,n,computers)

solution(3,[[1,1,0], [1,1,0], [0,0,1]])
