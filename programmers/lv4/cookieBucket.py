def solution(cookie):
    answer = 0
    left,right = 0,0
    leftSum,rightSum = 0,0
    for i in range(len(cookie) -1 ):
        left = i
        leftSum = cookie[i]
        right = i+1
        rightSum = cookie[i+1]
        while True:
            if leftSum == rightSum:
                answer = max(answer, leftSum)
            if leftSum > rightSum:
                right += 1
                if right == len(cookie) : 
                    break
                rightSum += cookie[right]
            else:
                left -=1 
                if left < 0 :
                    break
                leftSum += cookie[left]
    return answer

