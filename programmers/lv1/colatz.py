def solution(num):
    count = 0
    x = num
    if num == 1:
        return 0
    while count <=500 :
        if x%2 == 0 :
            x = x/2
            count += 1
            if x == 1:
                return count
        else :
            x = x*3+1
            count += 1      
            if x == 1:
                return count
        
    return -1



solution(1)