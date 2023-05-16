T = 1
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    b = list(map(int,input().split()))
    answer = 0
    
    for i in range(2,n-2):
        mid = b[i]
        left1 = b[i-1]
        left2 = b[i-2]
        right1 = b[i+1]
        right2 =b[i+2]

        if mid >= left1 and mid >=left2 and mid >= right2 and mid >=right1:
            maxFloor = max(right1,right2,left1,left2)
            answer += mid - maxFloor
            




    print("#"+str(test_case)+" "+ str(answer))
    
