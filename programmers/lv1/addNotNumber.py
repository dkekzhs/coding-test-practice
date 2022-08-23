
def solution(numbers):

    a = [0,1,2,3,4,5,6,7,8,9]
    b = list(set(a) - set(numbers))

    return sum(b)
solution([1,2,3,4,6,7,8,0])