n = 2
data = [("홍길동",95),("이순신",75)]
print(data)
data = sorted(data, key=lambda x : x[1], reverse= False)

for k,v in data:
    print(k,end = " ")