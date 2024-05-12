import sys
import heapq
input = sys.stdin.readline #이거 안쓰면 틀림

V,E = map(int,input().split())
K = int(input())

v_arr = [[] for _ in range(V+1)] #간선을 정점 별로 정리해두는 배열

INF = 1e8
d_arr = [INF]*(V+1) #거리를 넣어두는 배열 초기값은 가장 큰 값으로 한다.

for i in range(E):
    u,v,w = map(int, input().split())
    v_arr[u].append((v,w))


def dijkstra(start):
    q = [] #q에 정점까지의 거리와 정점을 넣어둔다.
    heapq.heappush(q,(0,start)) #시작점과 시작점은 0만큼 거리이기 때문에 초기값
    d_arr[start] = 0 #거리 배열에도 시작 지점을 0으로 초기화

    while q:
        dist,now = heapq.heappop(q) #우선순위가 가장 낮은 값이 나온다.
        #dist는 현재 노드까지의 거리 now는 현재 위치

        if d_arr[now] < dist: #d_arr에 저장되어있는 거리와 새로운 간선에서의 거리 비교
            continue#최단 거리가 아니면 스킵
        for i in v_arr[now]: #인접노드 처리
            if dist+i[1] < d_arr[i[0]]: #현재 노드 이전 노드까지 오는데 드는 비용과 이전 노드에서 현재 노드까지 가는데 드는 비용을 더한 값이 더 작을 떄
                d_arr[i[0]] = dist + i[1]
                heapq.heappush(q,(dist+i[1], i[0]))

dijkstra(K)
for i in range(1,len(d_arr)):
    if d_arr[i] == INF:
        print("INF")
    else:
        print(d_arr[i])