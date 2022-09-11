def solution(s):
    answer = ''
    for i in s.split(" "):
        answer += i.capitalize() + " "
    return answer[:-1]
