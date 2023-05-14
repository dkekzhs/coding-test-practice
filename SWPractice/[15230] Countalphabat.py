T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, T + 1):
    data = input()
    count = 0
    for i in range(len(data)):
        if chr(i+97) == data[i]:
            count+=1
        else: 
            break;
    print("#"+ str(test_case) + " "+ str(count))

