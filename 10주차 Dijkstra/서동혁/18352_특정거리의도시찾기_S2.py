import heapq
import sys
input = sys.stdin.readline

N, M, K, X = map(int,input().split())
# N < 300,000 , M < 1,000,000 , K < 300,000 , X < N

INF = 1e8

graph = [[] for i in range(N+1)] # 1번 노드부터 시작함

distance = [INF] * (N + 1) # 시작 노드로 부터 거리

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append((v,1)) # 각 길들은 weight가 1로 고정되어있다.

dijkstra = []

heapq.heappush(dijkstra,(0,X)) # 시작 노드의 거리를 0으로 설정
distance[X] = 0

while dijkstra:
    dist, now = heapq.heappop(dijkstra)

    if distance[now] < dist:
        continue

    for i in graph[now]:
        if dist + i[1] < distance[i[0]]:
            distance[i[0]] = dist + i[1]
            heapq.heappush(dijkstra,(dist + i[1], i[0]))

count = 0

for i in range(1,N+1):
    if distance[i] == K:
        count = count + 1
        print(i)

if count == 0:
    print(-1)

#https://velog.io/@tks7205/%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-with-python