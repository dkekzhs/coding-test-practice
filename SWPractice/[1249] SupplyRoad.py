import math
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y):
    answerList = [[math.inf for _ in range(N)] for _ in range(N)]
    answerList[0][0] = 0
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            xx = dx[i] + x
            yy = dy[i] + y

            if 0<= xx < N and 0<= yy <N:
                if answerList[x][y] + Map[xx][yy] < answerList[xx][yy]:
                    answerList[xx][yy] = answerList[x][y] + Map[xx][yy]
                    q.append((xx,yy))
    return answerList[-1][-1]

T = int(input())


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N= int(input())
    Map = [list(map(int,input())) for _ in range(N)]
    aa = bfs(0,0)
    print("#" + str(test_case) + " "+str(aa))

# 2
# 4
# 0100
# 1110
# 1011
# 1010
# 6
# 011001
# 010100
# 010011
# 101001
# 010101
# 111010







