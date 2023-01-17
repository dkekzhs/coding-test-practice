n = int(input())
arr = []
a = ""
for i in range(n):
    arr.append(input())


for j in range(n -1 ):
    for k in range(len(arr[j])):
        if arr[j][k] != arr[j+1][k]:
            a+="?"
        else: 
            a+=arr[j+1][k]
    arr[j+1] = a
    a=""

print(arr[len(arr)-1])
