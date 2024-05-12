import sys
import math
input = sys.stdin.readline

N, M = map(int, input().split())
# N < 1000 , M < 1000

stars = [[0, 0]] # 별들의 좌표 및 개수
edges = [] # 두 좌표 사이의 거리

root = list(range(N+1)) # 별의 index가 1부터 시작

mst_sum = 0.0
mst_count = 0

def find(x): # O(logN)
    while x != root[x]:
        x = root[x]
    
    return x

def union(a, b, cost): # O(2logN)
    global mst_sum
    global mst_count

    rootA = find(a)
    rootB = find(b)

    if rootA < rootB:
        rootA, rootB = rootB, rootA
    
    root[rootA] = rootB
    mst_sum = mst_sum + cost
    mst_count += 1
    
    if rootA == rootB: # cycle 생성
        mst_sum = mst_sum - cost
        mst_count -= 1

for index in range(N): # O(N)
    x, y = map(int, input().split())
    stars.append([x, y])

for i in range(M): # O(M * logN)
    x, y = map(int, input().split())
    union(x,y,0)

for i in range(1,N): # O(N * M) ??
    for j in range(i+1, N+1):
        edges.append([math.sqrt((stars[i][0] - stars[j][0]) ** 2 + (stars[i][1] - stars[j][1]) ** 2), i, j])

edges.sort() # O()

for edge in edges: 
    union(edge[1], edge[2], edge[0])

    if mst_count == N - 1:
        break

print("{:.2f}".format(mst_sum))
