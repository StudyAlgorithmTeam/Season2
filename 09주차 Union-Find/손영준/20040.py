import sys
input = sys.stdin.readline

n,m = map(int, input().split())
parent = list(range(n)) #각 노드를 부모 자기자신으로 초기화

def find(x): #find함수
    while x!= parent[x]:
        parent[x] = find(parent[x]) 
        #시간초과 때문에 부모 찾을 때마다 부모갱신 -> 경로압축
    return parent[x]

def union(x,y): #union함수
    root_x = find(x)
    root_y = find(y)
    if root_x < root_y:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y

result = 0
for i in range(m):
    x, y = map(int, input().split())
    # x와 y가 같은 집합이라면 현재 간선번호를 result로 설정.
    if find(x) == find(y): 
        result = i
        break
    union(x,y)
# 그치만 시간초과떠요 ㅠㅠ
print(result)
