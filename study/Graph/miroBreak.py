from collections import deque
N,M = 5,6
test = [
[1,0,1,0,1,0],
[1,1,1,1,1,1],
[0,0,0,0,0,1],
[1,1,1,1,1,1],
[1,1,1,1,1,1]]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(x,y):
    deq = deque()
    deq.append((x,y))

    while deq:
        x,y = deq.popleft()
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            if nx < 0 or ny < 0 or nx >= N or ny >= M :
                continue
            if test[nx][ny] == 0 :
                continue
            if test[nx][ny] == 1:
                test[nx][ny] = test[x][y] + 1
                deq.append((nx,ny))
    print(test)
    return test[N-1][M-1]

print(bfs(0,0))
