import re 
 
def solution(s):
    a = "[a-z]"
    return True if bool(re.findall(a,s.lower())) != True and (len(s) == 4 or len(s) == 6)  else False

solution("1234")