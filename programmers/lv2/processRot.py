def solution(rows, columns, queries):
    z= {}
    count = 0
    answer = []
    zz= []
    for x in range(1,rows+1):
        for i in range(1,columns+1):
            count+=1
            z[x,i] = count

    for a,b,c,d in queries:
        zz.clear()
        top,left,right,bottom = a,b,c,d
        tmp = z[(top,left)]
        zz.append(tmp)
        for k in range(top,right):
            z[(k,left)] = z[(k+1,left)]
            zz.append(z[(k+1,left)])
        for k in range(left,bottom):
            z[(right,k)] = z[(right,k+1)]
            zz.append(z[(right,k+1)])
        for k in range(right,top,-1):
            z[(k,bottom)] = z[(k-1,bottom)]
            zz.append(z[(k-1,bottom)])
        for k in range(bottom,left,-1):
            z[(top,k)] = z[(top,k-1)]
            zz.append(z[(top,k-1)])
        z[(top,left+1)] = tmp
        answer.append(min(zz))

    return answer

solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]])