a = int(input())
arr = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

arr.sort()
arr2.sort(reverse=True)

answer = 0 
for i in range(a):
    answer += arr[i] * arr2[i]
print(answer)

## 조건 정렬사용하지 않고 풀기
# a = int(input())
# arr = list(map(int,input().split()))
# arr2 = list(map(int,input().split()))
# answer = 0
# for i in range(a):
#     answer+= min(arr) * max(arr2)
#     arr.pop(arr.index(min(arr)))
#     arr2.pop(arr2.index(max(arr2)))
# print(answer)