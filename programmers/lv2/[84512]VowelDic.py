from itertools import product
def solution(word):
    answer = 0
    a = []
    z = ['A', 'E', 'I', 'O', 'U']
    for i in range(6):
        a.extend(list(product(z,repeat=i)))
    a = sorted(a,key = lambda x : x)
    bb = list(word)
    for aa in a : 
        if list(aa) == bb:
            answer = a.index(aa)
    
    return answer

solution("AAAAE")