time = 5 
count = 0
for i in range(time+1):
    for j in range(60):
        for k in range(60):
            if str(time) in str(i) + str(j)+str(k):
                count+=1
print(count)
