from sunau import AUDIO_FILE_ENCODING_LINEAR_16


def lcm1(ar1,ar2):

    for i in range(max(ar1,ar2),(ar1*ar2)+1):
        if i%ar1 == 0 and i%ar2 == 0:
            return i


def solution(arr):
    i = 1
    b = lcm1(arr[0],arr[1])
 
    while i< len(arr) -1:
        b = lcm1(b,arr[i+1])
        i+=1 
    return b

solution([2,6,8,14])