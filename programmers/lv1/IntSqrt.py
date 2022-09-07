import math
def solution(n):

    return int((math.sqrt(n)+1)*(math.sqrt(n)+1)) if int(math.sqrt(n)) >= math.sqrt(n) else -1

solution(3)