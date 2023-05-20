T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1): # A = P * 1리터 B = 기본요금 Q 월간 R 이하면기본요금만 R 보다 많으면 S 요금 수도양 W 리터
    P,Q,R,S,W = map(int,input().split())
    A = W * P
    B = Q
    if W > R :
        B += (W - R) * S
    print("#"+str(test_case), str(min(A,B)))



