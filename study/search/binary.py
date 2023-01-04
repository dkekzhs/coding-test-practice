
def binary_search(a,target,start,end):
    if start > end : 
        return None
    mid = (start+end)//2
    if a[mid] == target:
        return mid

    elif a[mid] > target:
        return binary_search(a,target,start,mid-1)
    else:
        return binary_search(a,target,mid+1,end)


b = [0,3,8,11,23,34]
find = 23
result = binary_search(b,find,0,len(b))

print(result)