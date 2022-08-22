def solution(nums):
    answer =0
    poketLen = int(len(nums)/2)
    a = set(nums)
    answer =min(len(a),poketLen)
    return answer