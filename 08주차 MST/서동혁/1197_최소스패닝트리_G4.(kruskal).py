import sys
input = sys.stdin.readline

V, E = map(int, input().split())
# 1 <= V <= 10,000 , 1 <= E <= 100,000

mst = list(range(V+1)) # list에 iterable 넣음 , range => iterable
edge_list = []
mst_sum = 0
mst_count = 0

def find(x) -> int:
    while x != mst[x]:
        x = mst[x]
    
    return x

def union(a, b, cost):
    global mst_sum
    global mst_count

    rootA = find(a)
    rootB = find(b)

    if rootA < rootB:
        rootA, rootB = rootB, rootA
    
    mst[rootA] = rootB
    mst_sum = mst_sum + cost
    mst_count += 1
    
    if rootA == rootB: # cycle 생성
        mst_sum = mst_sum - cost
        mst_count -= 1

for i in range(E):
    edge_list.append(list(map(int, input().split())))

edge_list.sort(key = lambda x : x[2])

for i in range(E):
    union(edge_list[i][0], edge_list[i][1], edge_list[i][2])

    if mst_count == V - 1:
        break

print(mst_sum)
