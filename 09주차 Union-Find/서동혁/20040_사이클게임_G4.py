import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# 3 <= N <= 500,000 , 3 <= M <= 1,000,000

root = list(range(N))
check = False
count = 0

def find(x): #O(logN)
    while x != root[x]:
        x= root[x]
    return x

def union(a, b): #O(2logN)
    global check
    rootA = find(a)
    rootB = find(b)

    if rootA < rootB:
        rootA, rootB = rootB, rootA
    elif rootA == rootB:
        check = True
    root[rootA] = rootB

for i in range(M): #O(M * logN)
    a, b = map(int, input().split())

    union(a,b)
    
    if check == True:
        count = i + 1
        break

print(count)
