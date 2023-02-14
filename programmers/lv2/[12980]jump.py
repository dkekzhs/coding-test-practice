def solution(n):
    ans = 0 
    a = str(bin(n)[2:])
    for i in a:
        if i == '1':
            ans +=1
    return ans
    

solution(5000)