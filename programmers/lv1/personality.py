# choices	뜻
# 1	매우 비동의
# 2	비동의
# 3	약간 비동의
# 4	모르겠음
# 5	약간 동의
# 6	동의
# 7	매우 동의


def solution(survey, choices):
    answer = ''
    s = {"R" : 0,
        "T"  : 0 ,
        "C"  : 0 ,
        "F"  : 0 ,
        "J"  : 0 ,  
        "M"  : 0 ,
        "A"  : 0 ,
        "N"  : 0 }
    for i in range(len(survey)):
        fir = survey[i][0]
        sec = survey[i][1]  
        if choices[i]  - 4 >0 :
            s[sec] += choices[i] -4
        elif choices[i] -4 <0 :
            s[fir] += 4 - choices[i]
                
    answer += "R" if s["R"] >= s["T"] else "T"
    answer += "C" if s["C"] >= s["F"] else "F"
    answer += "J" if s["J"] >= s["M"] else "M"
    answer += "A" if s["A"] >= s["N"] else "N"
    return answer