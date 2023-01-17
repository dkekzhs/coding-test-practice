def sqrtR(x):
    return x*x
def sqrt(x,x2):
    return (x-x2)**2
answer = []
for i in range(int(input())):
    stx,sty,enx,eny = list(map(int,input().split()))
    count = 0
    for j in range(int(input())):
        x,y,r = map(int,input().split())
        a = sqrt(stx,x) + sqrt(sty,y) < sqrtR(r)
        a2 = sqrt(enx,x) + sqrt(eny,y) < sqrtR(r)
        
        if a != a2:
            count+=1
            
    answer.append(count)

for z in answer:
    print(z)