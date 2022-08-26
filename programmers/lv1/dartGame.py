def solution(dartResult):
    jumsu = []
    opt = ["*","#"]
    cnt =0
    j=0
    for i in range(len(dartResult)):
        if i >=2 and dartResult[i-1] == "0" and dartResult[i-2] == "1":
            if dartResult[i] == "S":
                jumsu.append(10 ** 1)
                cnt+=1
            elif dartResult[i] == "D":
                jumsu.append(10 ** 2)
                cnt+=1
            elif dartResult[i] == "T":
                jumsu.append(10 ** 3)
                cnt+=1
        elif dartResult[i] == "S":
            jumsu.append(int(dartResult[i-1]) ** 1)
            cnt+=1
        elif dartResult[i] == "D":
            jumsu.append(int(dartResult[i-1]) ** 2)
            cnt+=1
        elif dartResult[i] == "T":
            jumsu.append(int(dartResult[i-1]) ** 3)
            cnt+=1
        if dartResult[i] == opt[0] or dartResult[i] == opt[1]:
            jumsu.append(dartResult[i])
    while cnt != len(jumsu):
        if j == 1 and jumsu[j] == "*":
            jumsu[j-1] = int(jumsu[j-1] *2)
            jumsu.pop(j)
        elif jumsu[j] == "#":
            jumsu[j-1] = int(jumsu[j-1] *-1)
            jumsu.pop(j)
        elif jumsu[j] == "*":
            jumsu[j-1] = int(jumsu[j-1] *2)
            jumsu[j-2] = int(jumsu[j-2] *2)
            jumsu.pop(j)
        j+=1
    print(jumsu)
    return sum(jumsu)

solution("1D2S#10S")