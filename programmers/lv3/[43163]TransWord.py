from collections import deque
def solution(begin, target, words):
    answer = 0
    visit = [False] * len(words)
    deq = deque([(begin,0)])
    n = len(words)
    m = len(begin)
    if target not in words:
        return answer
    answer=float('inf')
    while deq:
        w,cnt = deq.popleft()
        if w == target:
            answer = min(answer,cnt)
        for i in range(n):
            count = 0
            for j in range(m):
                if words[i][j] != w[j]:
                    count+=1
            if count == 1 and not visit[i]:
                visit[i] = True
                deq.append((words[i],cnt+1))
                
    return answer


                
solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"])