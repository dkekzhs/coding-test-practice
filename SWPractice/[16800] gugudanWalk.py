import math
T = int(input())

def sosu(x):
    num = 0
    for i in range(2,int(math.sqrt(x))+1):
        if n%i == 0:
            num = i
    if num == 0 :
        return x
    else:
        return num

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    num1 = sosu(n)
    answer = (n//num1)-1 + num1-1
    print("#"+str(test_case)+" "+ str(answer))











#input
# 3
# 10
# 50
# 10000000019

