def solution(board, moves):
    baguni = []
    answer = 0
    for i in moves :
        for j in board:
            if j[i-1] != 0:
                baguni.append(j[i-1])

                if(len(baguni)) > 1:
                    if( baguni[-2] == baguni[-1]):
                        del baguni[-2]
                        del baguni[-1]
                        answer +=2 
                j[i-1] = 0
                break  
    return answer


solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]	)
