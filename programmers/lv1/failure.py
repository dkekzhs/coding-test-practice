def solution(N, stages):
    answer = []
    av= []
    b=0
    v = len(stages)

    for i in range(1,N+1):
        if i in stages:
            b = stages.count(i)
            av.append([i,b/v])
            v -= b
            b=0 
        else : 
            av.append((i,0))
    av.sort(key = lambda x: x[1], reverse=True)
    for x,y in av:
        answer.append(x)

    print(answer)
    return answer


solution(5,	[2, 1, 2, 6, 2, 4, 3, 3])
solution(4,[4,4,4,4,4,4])