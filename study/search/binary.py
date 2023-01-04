def binary_search(a,target,start,end):
    if start > end : 
        return None
    mid = (start+end)//2
    if mid == target:
        return mid
    elif a[mid] > target:
        return binary_search(a,target,start,mid-1)
    else:
        return binary_search(a,target,mid+1,end)


b = [0,3,8,11,23,34]
find = 23
print(binary_search(b,find,0,len(b)))