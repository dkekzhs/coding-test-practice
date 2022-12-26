# n = input()
# a = list(map(str,input().split()))

n = 5
a = ["R","R","R","U","D","D"]

x,y = 1,1

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move = ["L","R","U","D"]
for plan in a:
    for i in range(len(move)):
        if plan == move[i]:
            ax = x + dx[i]
            ay = y + dy[i]
    if ax < 1 or ay <1 or ax> n or ay>n:
        continue
    x = ax
    y = ay
print(x,y)