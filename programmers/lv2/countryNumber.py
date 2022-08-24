def solution(n):
    
    rev_base = ''
    while n :
        if n%3 :
            print(n%3)
            n,mod =divmod(n,3)
            rev_base += str(mod)
        else:
            rev_base+="4"                      
            n = n//3-1
            

    print(rev_base[::-1])
    return rev_base[::-1] 
    

solution(4)