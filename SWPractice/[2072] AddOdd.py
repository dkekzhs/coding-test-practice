T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = list(map(int,input().split()))
    answer = 0 
    for i in range(len(n)):
        if n[i]%2 == 1:
            answer+= n[i]
    print("#"+str(test_case)+" " +str(answer))



# 3
# 3 17 1 39 8 41 2 32 99 2
# 22 8 5 123 7 2 63 7 3 46
# 6 63 2 3 58 76 21 33 8 1   