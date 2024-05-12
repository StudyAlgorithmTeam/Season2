import sys
import heapq
import math
INF = math.inf
input = sys.stdin.readline

n,m,k,x = map(int, input().split()) # 입력 받기
graph = [[] for _ in range(n+1)] # 노드간의 연결 저장하는 그래프
distance = [INF]*(n+1) # 최단거리 저장할 리스트 무한대로 초기화??

for _ in range(m):
    a,b = map(int, input().split()) # 간선의 양 끝점들 입력 받기
    graph[a].append(b)

q = [(0,x)] # 힙큐에 초기값을 0과 시작점으로 초기화
dist = [INF]*(n+1) # 최단거리 저장할 리스트를 무한대로 초기ㄹ화

dist[x] = 0 # 시작노드의 거리는 0으로 초기화

while q: # 갈 수 있는 점들 힙큐에서 꺼내서 확인.
    weight, node = heapq.heappop(q) #우선순위 큐에서 노드와 해당 노드까지의 거리를 빼온다.
    if dist[node] < weight: # 이미 최단거리가 갱신됨.
        continue
    # 현재 노드와 연결된 노드 검사
    for i in graph[node]:
        newWeight,newNode = 1,i # 새로운 노드 가중치는 1이다. 모든 가중치는 1임.
        distance = weight + newWeight
        # 새로운 거리가 기존 거리보다 짧다면 업데이트후 우선순위큐에 넣음.
        if dist[newNode]> distance:
            dist[newNode] = distance
            heapq.heappush(q,(distance,newNode)) # 다시 넣는다.
        else:
            continue

# 특정값 k와 같은 노드 출력 없다면 -1
if dist.count(k) == 0:
    print(-1)
else:
    for j in range(1,n+1):
        if dist[j] == k:
            print(j)

