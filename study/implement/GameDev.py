m,n = 4,4
x,y,direction = 1,1,0
Map = [[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]

visit = [[0 for _ in range(m)] for _ in range(n)] 
visit[x][y] = 1

dx = [-1,0,1,0]
dy = [0,1,0,-1]


def trun_left():
    global direction
    direction -=1 
    if direction == -1 :
        direction =3
    
count = 0
trun_time = 0
while True:
    trun_left()
    nx = x+ dx[direction]
    ny = y+ dy[direction]

    if visit[nx][ny] ==0 and Map[nx][ny] ==0 :
        visit[nx][ny] = 1
        x = nx
        y = ny 
        count += 1
        trun_time = 0
        continue
    else : 
        trun_time += 1
    if trun_time == 4:
        nx = x -dx[direction]
        ny = y -dy[direction]
        
        if Map[nx][ny] == 0 :
            x = nx
            y = ny
        
        else : 
            break
        trun_time = 0
print(count)