import sys
from itertools import combinations
n,k = map(int,input().split())

answer = 0 
words = [set(sys.stdin.readline().rstrip()) for _ in range(n)]
common_word = {'a','c','t','n','i'}
alphabat = set(chr(i) for i in range(97,123)) - common_word

learn = [0] * 123

for i in common_word:
    learn[ord(i)] = 1


def readCnt(data,learned):
    cnt = 0 
    for word in data:
        canRead = 1
        for w in word:
            if learned[ord(w)] == 0:
                canRead = 0
                break
        if canRead == 1:
            cnt+=1 
    return cnt
if k >=5:
    for teach in list(combinations(alphabat,k-5)):
        for t in teach:
            learn[ord(t)] = 1
        cnt = readCnt(words,learn)

        if cnt > answer :
            answer = cnt

        for t in teach:
            learn[ord(t)] = 0
    print(answer)        
else:
    print(0)


