T = int(input())

def SumData(i,j,M,FlyMap):
    data = 0 
    for k in range(i,i+M):
        for z in range(j,j+M):
            data += FlyMap[k][z]
    return data

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    young = N-M+1
    answerList = []
    FlyMap = []
    for i in range(N):
        FlyMap.append(list(map(int,input().split())))

    for i in range(young):
        for j in range(young):
            answerList.append(SumData(i,j,M,FlyMap))
    print("#"+str(test_case)+ " " + str(max(answerList)))
        