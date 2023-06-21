from collections import deque

def solution(picks,minerals):
    answer = 0
    keys = {'diamond' : 0 , 'iron' : 1 , 'stone' : 2}
    mined = [[1,1,1],[5,1,1],[25,5,1]]
    minerals = minerals[:5 * sum(picks)]
    deq = deque(minerals)
    data = []
    while deq :
        Maxmine = 0 
        Dia,Iro,Sto = 0,0,0
        while Maxmine<5:
            Maxmine+=1
            mine = deq.popleft()
            Dia += mined[0][keys[mine]]
            Iro += mined[1][keys[mine]]
            Sto += mined[2][keys[mine]]
            if not deq:
                break
        data.append([Dia,Iro,Sto])
    data.sort(key = lambda x : [x[2],x[1],x[0]])
    for idx, p in enumerate(picks):
        for _ in range(p):
            if data:
                answer += data.pop()[idx]
            else:
                return answer
    return answer

# solution([1, 0, 1],["iron", "iron", "iron", "iron", "diamond", "diamond", "diamond"])
# solution(	[1, 0, 1], ["stone", "stone", "stone", "stone", "stone", "iron", "iron", "iron", "iron", "iron", "diamond", "diamond"])
solution([1, 3, 2],["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"])
# solution([0, 1, 1],["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"])