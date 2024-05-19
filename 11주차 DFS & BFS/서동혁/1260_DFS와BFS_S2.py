import heapq
from collections import deque

N, M, V = map(int,input().split())

graph_dfs = [[] for i in range(N+1)]
graph_bfs = [[] for i in range(N+1)]
visit_dfs = [False] * (N+1)
visit_bfs = [False] * (N+1)

for i in range(M):
    s, e = map(int, input().split())

    heapq.heappush(graph_dfs[s], e) # 힙을 이렇게도 써도 되네??
    heapq.heappush(graph_dfs[e], s)
    heapq.heappush(graph_bfs[s], e)
    heapq.heappush(graph_bfs[e], s)
    # graph[s].append(e) => 작은 순서대로 탐색이 안되네 => sort하면 가능하긴함
    # graph[e].append(s)

def dfs(v):
    visit_dfs[v] = True
    print(v, end=" ")
    while(graph_dfs[v]):
        i = heapq.heappop(graph_dfs[v])
        if visit_dfs[i] == False:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visit_bfs[v] = True

    while queue:
        tmp = queue.popleft()
        print(tmp, end=" ")
        while graph_bfs[tmp]:
            check = heapq.heappop(graph_bfs[tmp])
            if visit_bfs[check] == False:
                queue.append(check)
                visit_bfs[check] = True
dfs(V)
print()
bfs(V)

# dfs https://siloam72761.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%89%BD%EA%B2%8C-%EC%9D%B4%ED%95%B4%ED%95%98%EB%8A%94-DFS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%A0%95%EC%9D%98-%ED%8A%B9%EC%A7%95-%EC%BD%94%EB%93%9C