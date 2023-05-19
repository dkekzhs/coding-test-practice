# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    dump = int(input())
    data = list(map(int,input().split()))
    data.sort()
    for i in range(dump):
        data[0] = data[0] +1
        data[99] = data[99] -1
        data.sort()
    print("#"+str(test_case)+" "+ str(max(data) - min(data)))