
def solution(n,a,b):
    answer = 1
    while True:
        if (a %2 == 0 and a-1 ==b) or (a%2 !=0 and a+1 ==b ):
            return answer
        a = rere(a)
        b = rere(b)
        answer+=1

def rere(x):
    if x % 2 == 0 :
        return int(x//2)
    else:
        return int((x/2)+1)


solution(8,4,7)