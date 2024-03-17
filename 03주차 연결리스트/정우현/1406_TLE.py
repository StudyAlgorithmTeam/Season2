from collections import deque

L = str(input())
T = int(input())

R = list(L)
k = len(R)

for i in range(T):
    
    j = str(input())
    a = list(j)
    if a[0] == 'L':
        if k>0:
            k-=1
    elif a[0] == 'D':
        if k<len(R):
            k+=1
    elif a[0] == 'B':
        if k>0:
            R.remove(R[k-1])
    elif a[0] == 'P':
        R.insert(k,a[2])
        k+=1

print(*R,sep='')
