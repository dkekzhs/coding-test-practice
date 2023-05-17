from collections import deque

def bfs(N, K):
    visited = set()
    visited.add((N, 0))
    q = deque()
    q.append((N, 0))
    answer = 0
    M = len(str(N))
    while q:
        n, k = q.popleft()
        if k == K:
            answer = max(answer, n)
            continue
        n = list(str(n))
        for i in range(M-1):
            for j in range(i+1, M):
                if i == 0 and n[j] == '0':
                    continue
                n[i], n[j] = n[j], n[i]
                nn = int(''.join(n))
                if (nn, k+1) not in visited:
                    q.append((nn, k+1))
                    visited.add((nn, k+1))
                n[i], n[j] = n[j], n[i]
    return answer 
        

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,K =  map(int, input().split())
    answer = bfs(N,K)
    print("#"+str(test_case)+" " +str(answer))
    