from collections import deque
def solution(msg):
    answer = []
    msg = deque(msg)
    dic = {}
    for i in range(1,27):
        dic[chr(64+i)] = i

    k=""
    v=27
    while msg:
        k += msg.popleft()

        if msg:
            if k + msg[0] not in dic.keys():
                dic[k+msg[0]] = v 
                v += 1
                answer.append(dic[k])
                k = ""
    answer.append(dic[k])
    return answer


solution("KAKAO")