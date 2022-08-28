def solution(s):
    answer = len(s)
    for i in range(1,len(s)//2 +1):
        x = ""
        pre = s[0:i]
        count = 1
        for j in range(i,len(s),i):
            if pre == s[j:j + i]:
                count +=1
            else:
                x += str(count) + pre if count>=2 else pre
                pre = s[j:j+i]

                count = 1
        x += str(count) + pre if count>=2 else pre
        answer = min(answer, len(x))       

    print(answer)

    return answer

solution("aabbaccc")