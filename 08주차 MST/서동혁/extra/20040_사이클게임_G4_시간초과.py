N, M = map(int, input().split())
# 3 <= N <= 500,000 , 3 <= M <= 1,000,000

root = list([i for i in range(N)])

def find(x):
    if (root[x] == x):
        return x
    else:
        return find(root[x])

def union(a, b, count):
    rootA = find(a)
    rootB = find(b)

    root[rootA] = rootB

    if rootA == rootB:
        return count
    
count = 0

for i in range(M):
    a, b = map(int, input().split())

    if union(a, b, i+1) == i + 1:
        count = i+1
        print(count)
        break

if count == 0:
    print(count)
