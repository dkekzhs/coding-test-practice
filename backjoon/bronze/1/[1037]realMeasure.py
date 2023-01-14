import math
n = int(input())
a = list(map(int,input().split()))
max_a = max(a)
min_a = min(a)
print(math.lcm(max_a,min_a) * math.gcd(max_a,min_a))
