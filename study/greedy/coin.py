# 그리디 알고리즘 코인선택
def greed_coin(N,coins):
    count = 0
    for coin in coins:
        count+= N//coin
        N %=coin
    print("최소 동전 " ,count)
    
N = 1260
coins = [500,100,50,10]
greed_coin(N,coins)