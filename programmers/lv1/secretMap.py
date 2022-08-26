def dem(n):
    rev_base = ''
    while n :
        n,mod =divmod(n,2)
        rev_base += str(mod)
    return rev_base[::-1]


def solution(n, arr1, arr2):
    answer = []
    to_insert  = "0"
    c= ""
    for i in range(len(arr1)):
        a = dem(arr1[i])
        b = dem(arr2[i])
        while len(a) != n:
            a = to_insert + a
        while len(b) != n:
            b = to_insert + b
        for i in range(0,n):
            if a[i] == "1" or b[i] == "1":
                c+="#"
            else : 
                c+= " "
        answer.append(c)
        c=""

        print(a, b)
    print(answer)
    return answer

solution(5,[9,20,28,18,11],[30,1,21,17,28])