def solution(x):
    b= 0
    for i in str(x):
        b += int(i)
    
    return True if x%b == 0 else False

solution(19)