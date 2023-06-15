from itertools import permutations
## 내가 푼 방법 , 던전 최대길이 8, 모든조합 탐색해도 시간 될거 같아서 이렇게 품 
def solution(k, dungeons):
    temp = [i for i in range(len(dungeons))]
    temp = list(permutations(temp,len(dungeons)))
    count = []
    for i in range(len(temp)):
        tempData = k 
        count2 = 0 
        for da in temp[i]:
            if tempData >= dungeons[da][0]:
                tempData = tempData- dungeons[da][1]
                count2+=1
        count.append(count2)
    

    return max(count)


## dfs 풀이법
answer = 0
N = 0
visited = []

def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt
    for j in range(N):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            visited[j] = 0


def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer

solution(80,[[80,20],[50,40],[30,10]])