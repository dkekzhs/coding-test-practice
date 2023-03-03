from itertools import combinations
def solution(number):
    answer = 0
    a = combinations(number,3)
    for i in a:
        if sum(i) == 0:
            answer+=1

    print(answer)
    return answer

solution([-2, 3, 0, 2, -5])