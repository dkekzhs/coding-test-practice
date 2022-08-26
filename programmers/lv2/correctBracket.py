def solution(s):
    open =0
    close =0

    for i in range(len(s)):    
        if s[0] == ")":
            return False
        elif s[len(s) -1]  == "(":
            return False
        elif close > open :
            return False
        else:
            if s[i] == "(":
                open +=1
            else :
                close += 1
    if open - close ==0:
        print(open , close)
        return True
    else : 
        return False
    

solution("(()))(()")