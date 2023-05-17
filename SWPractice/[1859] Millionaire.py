T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    data = list(map(int,input().split()))
    result = 0
    max_num = 0
    for i in range(len(data)-1,-1,-1):
        if data[i] > max_num:
            max_num = data[i]
        else:
            result += max_num-data[i]
    print("#"+str(test_case)+" "+str(result))

# 3
# 3
# 10 7 6
# 3
# 3 5 9
# 5
# 1 1 3 1 2