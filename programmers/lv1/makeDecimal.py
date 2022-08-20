from itertools import combinations

def decimal(nums):
    for i in range(2, nums):
        if nums % i == 0:
            return False
    
    return True
        
def solution(nums):
    answer = 0
    a = list(combinations(nums, 3))
    for i in a:
        if decimal(i[0] + i[1] + i[2]) :
            answer += 1
    print(answer)
    return answer

solution([1,2,3,4])