from collections import deque

def solution(maps):
    
    dy,dx = [-1,0,1,0],[0,1,0,-1]
    deq = deque()
    deq.append((0,0))
    maxX = len(maps)
    maxY = len(maps[0])
    visit = [[0 for _ in range(maxY)] for _ in range(maxX)]
    visit[0][0] = 1
    while deq:
        y,x = deq.popleft()
        for i in range(4):
            ny,nx = y+dy[i] , x+dx[i]
            if 0<= ny < maxX and 0<= nx < maxY:
                if visit[ny][nx] == 0 and maps[ny][nx] == 1:
                    visit[ny][nx] = visit[y][x]+ 1
                    deq.append((ny,nx))
    if visit[maxX-1][maxY-1] == 0 :
        return -1 
    else:
        return visit[maxX-1][maxY-1] 
