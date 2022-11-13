def solution(citations):
    answer= 0
    a = len(citations)
    citations.sort(reverse  = True)
    for i in range(a):
        if i +1 <=citations[i]:
            answer += i+1
        if i+1 > citations[i]:
            break
    return answer

solution([5,4,3,8,10])