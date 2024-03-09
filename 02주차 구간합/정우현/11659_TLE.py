def plusN(i,j,Narr):
    result = 0
    for c in range(i,j+1):
        result += Narr[c]
    return result
    
N,M = map(int, input().split())
Narr = list(map(int, input().split()))
Narr.insert(0,0)
rarr = []

for i in range(M):
    ii, jj = map(int,input().split())
    if ii == jj:
        rarr.append(Narr[ii])
    else:
        Z = plusN(ii,jj,Narr)
        rarr.append(Z)

print(rarr,sep ='\n')
