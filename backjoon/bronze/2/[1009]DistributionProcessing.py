

for _ in range(int(input())):
    a,b = map(int,input().split())
    result = [(a ** i) % 10 for i in range(1,5)][(b % 4) -1]
    print(result if result != 0 else 10)





