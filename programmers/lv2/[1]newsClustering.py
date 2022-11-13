from collections import Counter
def solution(str1, str2):

    arr1 = [str1[i:i+2].lower() for i in range(len(str1) - 1) if str1[i:i+2].isalpha()]
    arr2 = [str2[i:i+2].lower() for i in range(len(str2) - 1) if str2[i:i+2].isalpha()]

    if len(arr1) == 0 and len(arr2) == 0:
        return 65536

    cnt1 = Counter(arr1)
    cnt2 = Counter(arr2)
    sum1 = sum((cnt1|cnt2).values())
    sum2 = sum((cnt1&cnt2).values())


    return int((sum2/sum1)*65536)
