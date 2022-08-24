import itertools
def solution(numbers):
    answer = []

    a = itertools.combinations(numbers,2)

    for i in a:
        b = i[0] + i[1]
        if b not in answer:
            answer.append(b)
   
    return sorted(answer)

solution([2,1,3,4,1])