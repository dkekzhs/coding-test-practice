def solution(record):
    answer = []
    a = [i.split(" ") for i in record]
    dic ={}

    for i in a: 
        if i[0] =="Enter":
            dic[i[1]] = i[2]
        elif i[0] == "Change":
            dic[i[1]] = i[2]
    
    for j in a:
        if j[0] == "Enter":
            answer.append(dic[j[1]]+"님이 들어왔습니다.")
        elif j[0] == "Leave":
            answer.append(dic[j[1]]+"님이 나갔습니다.")

    return answer

solution(["Enter uid1234 Muzi", 
"Enter uid4567 Prodo",
"Leave uid1234",
"Enter uid1234 Prodo",
"Change uid4567 Ryan"])