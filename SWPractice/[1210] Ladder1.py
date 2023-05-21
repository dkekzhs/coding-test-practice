from collections import deque

def dfs(i,k,Map):
    ch = [[0] * 100 for _ in range(100)]
    deq = deque()
    ch[1][i] = 1
    deq.append((i,1))
    
    while deq:
        x,y = deq.popleft()
        if Map[y][x] == k:
            return i
        if y >= 99 :
            return False
        if 0<x<100:
            if x+1 == 100:
                if not ch[y+1][x] and (Map[y+1][x] == 1 or Map[y+1][x] == 2) and Map[y][x-1] == 0 :
                    deq.append((x,y+1))
                elif not ch[y][x-1] == 1 or Map[y][x-1] == 1:
                    if not ch[y][x-1] and Map[y][x-1] == 1:
                        deq.append((x-1,y))
                    elif not ch[y+1][x] and (Map[y+1][x] == 1 or Map[y+1][x] == 2):
                        deq.append((x, y+1))
            else:
                if not ch[y+1][x] and (Map[y+1][x] == 1 or Map[y+1][x] == 2) and Map[y][x+1] == 0 and Map[y][x-1] == 0:
                    deq.append((x,y+1))
                elif Map[y][x+1] == 1 or Map[y][x-1] == 1 :
                    if not ch[y][x+1] and Map[y][x+1] == 1:
                        deq.append((x+1,y))
                    elif not ch[y][x-1] and Map[y][x-1] == 1:
                        deq.append((x-1,y))
                    elif not ch[y+1][x] and (Map[y+1][x] == 1 or Map[y+1][x] == 2):
                        deq.append((x,y+1))
        elif x==0:
            if not ch[y+1][x] and (Map[y+1][x] == 1 or Map[y+1][x] == 2) and Map[y][x+1] == 0 :
                deq.append((x,y+1))
            elif Map[y][x+1] ==1:
                if not ch[y][x+1] and Map[y][x+1] == 1:
                    deq.append((x+1,y))
                elif not ch[y+1][x] and (Map[y+1][x] ==1 or Map[y+1][x] == 2):
                    deq.append((x,y+1))
        ch[y][x] = 1
    
    


            
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다. 맵 앞에 y 좌표 뒤에꺼 x좌표
for test_case in range(1, 11):
    N = 100
    T = int(input())

    Map = [list(map(int,input().split()))for _ in range(N)]
    
    for i in range(N):
        if Map[0][i] == 1:
            a = dfs(i,2,Map)
            if a:
                print("#"+str(T)+" "+ str(a))

