import math

def solution(numbers, hand):
    dic = {1 : [0,0],
    2 : [0,1],
    3 : [0,2],
    4 : [1,0],
    5 : [1,1],
    6 : [1,2],
    7 : [2,0],
    8 : [2,1],
    9 : [2,2],
    "*" : [3,0],
    0 : [3,1],
    "#" : [3,2]}
    handL = "*"
    handR = "#"
    answer = ''

    for i in numbers : 
        if i == 1 or i == 4 or i ==7 :
            handL = i
            answer += "L"
        elif i == 3 or i == 6 or i ==9 :
            handR = i
            answer += "R"
        else :
            x = dic.get(i)[0]
            y = dic.get(i)[1]
            l_x = dic.get(handL)[0]
            l_y = dic.get(handL)[1]
            r_x = dic.get(handR)[0]
            r_y = dic.get(handR)[1]
            
            l_d = math.ceil(math.sqrt(math.pow(x - l_x ,2) + math.pow(y - l_y,2)))
            r_d = math.ceil(math.sqrt(math.pow(x - r_x ,2) + math.pow(y - r_y,2)))
            if l_d < r_d:
                handL = i
                answer += "L"
            elif r_d < l_d :
                handR = i
                answer += "R"
            else:
                if hand == "left":
                    handL = i
                    answer += "L"
                else:
                    handR = i
                    answer += "R" 

    return answer
