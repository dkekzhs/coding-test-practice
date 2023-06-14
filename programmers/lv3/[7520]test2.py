from collections import deque
def solution(s):
    answer = []

    for string in s:
        count = 0
        stack = []
        for s in string:
            if s == "0":
                if stack[-2:] ==['1','1']:
                    count+=1
                    stack.pop()
                    stack.pop()
                else:
                    stack.append(s)
            else:
                stack.append(s)
        if count == 0:
            answer.append(string)
        else:
            deq = deque()

            while stack:
                if stack[-1] == "1":
                    deq.append(stack.pop())
                elif stack[-1] == "0":
                    break
            while count > 0 :
                deq.appendleft("0")
                deq.appendleft("1")
                deq.appendleft("1")
                count -=1

            while stack:
                deq.appendleft(stack.pop())
            answer.append("".join(deq))
    


    return answer


solution(["1110","100111100","0111111010"])