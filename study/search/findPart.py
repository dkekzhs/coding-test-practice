N = 5
part = [8,3,7,9,2]
M = 3
find = [5,7,9]


for i in range(M):
    if find[i] in part:
        print("yes" , end=" ")
    else:
        print("No" , end=" ")

part.sort()

def bin_search(a,f,start,end):
    while start<= end:
        mid = (start+end) // 2
        if a[mid] == f:
            return mid
        elif a[mid] > f:
            end = mid -1
        else:
            start = mid +1
    return None



for x in find:
    result = bin_search(part,x,0,N-1)
    if result == None:
        print("no", end=" ")
    else :
        print("yes", end = " ")

