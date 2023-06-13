from itertools import permutations
def bigo(user,ban):
    for user_len in range(len(user)):
        if len(user[user_len]) != len(ban[user_len]):
            return False
        for zz in range(len(user[user_len])):
            if user[user_len][zz] != ban[user_len][zz] and ban[user_len][zz] != "*":
                return False
    
    return user
def solution(user_id, banned_id):
    a = []
    tempList = list(permutations(user_id,len(banned_id)))
    for i in range(len(tempList)):
        tem = bigo(tempList[i],banned_id)
        if tem != False:
            if set(tem) not in a:
                a.append(set(tem))
        
    
    
    

    return len(a) 

solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"])
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"])
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"])