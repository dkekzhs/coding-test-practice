from collections import Counter
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    data = list(map(int,input().split()))
    a = Counter(data)
    print("#"+str(N)+" "+ str(a.most_common(1)[0][0]))