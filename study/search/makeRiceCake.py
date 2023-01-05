N = 4 
M = 6
RiceCake =  [19,15,10,17]


RiceCake.sort()

start = 0
end = max(RiceCake)
result =0
while start <= end :
    total = 0
    mid = (start+end)//2
    for x in RiceCake:
        if x > mid:
            total += x - mid
    if total < M:
        end = mid -1

    else : 
        result = mid
        start = mid +1

print(result)
