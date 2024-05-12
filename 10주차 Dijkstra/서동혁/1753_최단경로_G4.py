import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split()) # V < 20,000 , E < 300,000
K = int(input()) # 시작 노드 번호

INF = 1e6 # V의 최대 갯수 ==> 20000이고 모든 간선이 10이라고 하면 200,000 까지 가능함.

graph = [[] for _ in range(V+1)] # 각 정점들과의 연결된 간선들
distance = [INF] * (V+1) # 시작점으로부터의 거리

for _ in range(E):
    u, v , w = map(int, input().split())
    graph[u].append((v,w))

dijkstra = []

heapq.heappush(dijkstra,(0,K))
distance[K] = 0

while dijkstra:
    dist, now = heapq.heappop(dijkstra)

    if distance[now] < dist: # 만약 dis[now]가 dist 보다 작다면 이미 방문을 한 노드이므로 건너뛴다.  
        continue

    for i in graph[now]:
        if dist + i[1] < distance[i[0]]:
            distance[i[0]] = dist + i[1]
            heapq.heappush(dijkstra,(dist + i[1],i[0]))
# ex) 처음에 1에서 1로 가는 경우는 distance[1] = 0이고 dist도 0이다. 백준의 예시를 보면 graph[1] 에는 (2,2) (3,3)이 있기에
# 1->1->2 경로값인 0 + 2와 distance[2]인 INF 값을 비교한다. 마찬가지고 1->1->3도 동일하다.
for i in range(1,V+1):
    if distance[i] == INF:
        print("INF")
        continue
    print(distance[i])

