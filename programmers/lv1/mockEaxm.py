def solution(answers):
    score = [0, 0, 0]
    fir = [1,2,3,4,5]
    sec = [2,1,2,3,2,4,2,5]
    thr = [3,3,1,1,2,2,4,4,5,5]
    answer = []

    for i in range(len(answers)):
        if(answers[i] == fir[i%len(fir)]):
            score[0] += 1
        if(answers[i] == sec[i%len(sec)]):
            score[1] += 1
        if(answers[i] == thr[i%len(thr)]):
            score[2] += 1
    
    max1 = max(score)
    for i in range(3):
        if score[i] == max1:
            answer.append(i + 1)
        

    print(answer)

    return answer
    
