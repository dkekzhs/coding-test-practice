import math
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    answer = 0
    for i in range(-n-1,n+1):
        for j in range(-n-1,n+1):
            if int(math.pow(i,2)) + int(math.pow(j,2)) <= int(math.pow(n,2)):
                answer+=1
    print("#"+str(test_case) +" "+ str(answer))
