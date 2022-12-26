def greedy_big(n,m,k,data):
    data.sort()
    fir = data[len(data)-1]
    sec = data[len(data)-2]
    count = 0
    answer= 0  
    for _ in range(m):
        if count == k:
            count = 0 
            answer+= sec 
            continue
        else: 
            answer += fir
            count+=1
    return answer

def greedy_big2(i1,i2):
    n,m,k = map(int,i1.split())
    data = list(map(int,i2.split()))
    data.sort()

    result = 0

    fir = data[len(data) - 1]
    sec = data[len(data) - 2]
    while True :
        for _ in range(k):
            if m == 0 :
                break
            result += fir
            m -= 1
        if m == 0 :
            break
        result += sec
        m-= 1
    print(result)


#수열로 구현 
def greedy_big3(i1,i2):
    n,m,k = map(int,i1.split())
    data = list(map(int,i2.split()))
    data.sort()
    fir = data[len(data) - 1]
    sec = data[len(data) - 2]
    result = 0

    count = int(m/ (k+1)) * k
    count += m % (k+1)
    result += count * fir
    result += (m - count) *sec
    print(result)

i1 = "5 8 3"
i2 = "2 4 5 4 6"

greedy_big2(i1,i2)
greedy_big3(i1,i2)

n,m,k = 5,8,3
data = [2,4,5,4,6]

print(greedy_big(n,m,k,data))
