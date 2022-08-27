def solution(strings, n):
    dic = {}
    for i in strings:
       dic[i] =  ord(i[n])
    d1 = dict(sorted(dic.items()))
    d2 = dict(sorted(d1.items(), key = lambda x : x[1]))

    return [i for i in d2] 

solution(["abce", "abcd", "cdx"],2)