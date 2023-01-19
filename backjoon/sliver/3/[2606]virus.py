n = int(input())
m = int(input())
arr = [[]for _ in range(n+1)]
for i in range(m):
    q,w = map(int,input().split())
    arr[q].append(w)
    arr[w].append(q)

visit_Value = [False] * (n+1)
count = 0

def dfs(visit):
    global count
    visit_Value[visit] = True
    
    for k in arr[visit]:
        if not visit_Value[k]:
            dfs(k)
            count+=1
            

dfs(1)
print(count)