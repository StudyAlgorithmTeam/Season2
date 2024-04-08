V_count, E_count = map(int, input().split())

parent = [0]
V_set = {}

for i in range(1, V_count+1):
    parent.append(i)

edges = []
total_cost = 0

# 간선 정보 입력
for i in range(E_count):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))  # 비용 순 정렬을 위해 cost를 첫번째로 저장

edges.sort()

# 부모 노드 찾기 함수
def find_parent(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 부모 노드 합치기 함수
def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for edge in edges:
    if find_parent(parent, edge[1]) == find_parent(parent, edge[2]):
        continue
    else:
        total_cost += edge[0]
        union(parent, edge[1], edge[2])

print(total_cost)
