import sys
import heapq
import math

INF = math.inf
input = sys.stdin.readline

n,m = map(int, input().split()) # 입력 받기
start = int(input())
graph = [[] for _ in range(n+1)] # 노드간의 연결 저장하는 그래프
distance = [INF]*(n+1) # 최단거리 저장할 리스트 무한대로 초기화??

for _ in range(m):
    u,v,w = map(int, input().split()) # 간선의 양 끝점들 입력 받기
    graph[u].append((v,w))

q = [(0,start)] # 힙큐에 초기값을 0과 시작점으로 초기화
distance[start] = 0 # 시작노드의 거리는 0으로 초기화

while q: # 갈 수 있는 점들 힙큐에z서 꺼내서 확인.
    weight, node = heapq.heappop(q)
    if distance[node] < weight: # 이미 최단거리가 갱신됨.
        continue
    # 현재 노드와 연결된 노드 검사
    for newNode ,newWeight in graph[node]:
        new_distance = weight + newWeight
        # 똑같이 짧으면 업데이트하고 아니면 무시
        if distance[newNode]> new_distance:
            distance[newNode] = new_distance
            heapq.heappush(q,(new_distance,newNode))


for i in range(1,n+1):
    if distance[i] == INF:
        print("INF")
        continue
    else:
        print(distance[i])

  '''졸려서 자러갑니다..ㅠㅠ 넘 어려워'''
