def solution(numbers, target):
    answers = [0]
    answer = 0

    for num in numbers:
        tmp =[]
        for j in answers:
            tmp.append(j + num)
            tmp.append(j - num)
        answers = tmp
    for z in answers:
        if z == target:
            answer+=1 

    print(answer,answers)
    return answer

solution([1,1,1,1,1],3)