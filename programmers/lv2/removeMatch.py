def solution(s):
    if len(s)%2 != 0:
        return 0
    stack = []
    for i in range(len(s)):
        
        if len(stack) == 0 or stack[-1] != s[i]:
            stack.append(s[i])
        elif(stack[-1]== s[i]):
            stack.pop()
    return 0 if len(stack) else 1
solution("cdcdz")