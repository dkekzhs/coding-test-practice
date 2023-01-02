a = [1,3,2,4,5,0]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    tail = arr[1:]
    left = [x for x in tail if x<= pivot]
    right = [x for x in tail if x> pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)
print(quick_sort(a))


def quick(a,start,end):
    if start>=end:
        return 
    pivot = start
    left = start+1
    right = end
    while left<= right:
        while left <= end and a[left] <= a[pivot]:
            left+=1

        while right> start and a[right] >= a[pivot]:
            right -=1 
        if left> right:
            a[right],a[pivot] = a[pivot],a[right]
        else:
            a[left],a[right] = a[right],a[left]
    quick(a,start,right-1)
    quick(a,right+1,end)
quick(a,0,len(a)-1)
print(a)
