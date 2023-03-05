def solution(n, m, section):
    answer = 0
    temp = max(section)+1
    for i in reversed(range(0,len(section))):

        if temp <= section[i]:
            continue
        
        answer+=1
        temp = section[i] -m +1
        if temp <0:
            break
    

    print(answer)
    
    return answer

solution(8,4,[2, 3, 6])
solution(5,4,[1, 3]	)
solution(4,1,[1, 2, 3, 4])