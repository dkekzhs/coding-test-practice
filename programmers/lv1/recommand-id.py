import re

def solution(new_id):
    answer = ""
    b = ['-','_','.']
    pattern = '[a-z]'
    answer = new_id.lower()
    
    for i in answer:
        if b[0] == i or b[1] == i or b[2] == i or re.findall(pattern, i) or re.findall("\d",i):
            pass
        else :
            answer =  answer.replace(i,"")
    while ".." in answer:
        answer = answer.replace("..",".")   
    


    if (answer[0] =="."):
       answer = answer.lstrip(".")
    if answer == "":
        answer = "a"
    if(answer[len(answer) -1 ] =="."):
      answer = answer.rstrip(".")

    if(len(answer) >15):
        answer =answer[:15]

    if(answer[len(answer ) -1 ] == "."):
        answer = answer.rstrip(".")
    if len(answer) <= 3:
        answer = answer + answer[-1] * (3-len(answer))
    
    print(answer)
    return answer
