import sys
import math
input = sys.stdin.readline

N = int(input())

stars = []
edges = []
root = list(range(N))
mst_sum = 0
mst_count = 0

def find(x):
    while x != root[x]:
        x = root[x]
    
    return x

def union(a, b, cost):
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

for index in range(N): # x, y 좌표와 각 별들마다 index를 부여
    x, y = map(float, input().split())
    stars.append([x, y])

for i in range(N-1):
    for j in range(i+1, N):
        edges.append([math.sqrt((stars[i][0] - stars[j][0]) ** 2 + (stars[i][1] - stars[j][1]) ** 2), i, j])

edges.sort()

for edge in edges:
    union(edge[1], edge[2],edge[0])

    if mst_count == N - 1:
        break

print(mst_sum)
