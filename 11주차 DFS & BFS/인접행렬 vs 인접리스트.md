## 인접 행렬 방식

$O(V^2)$

```python
n,m,v = map(int, input().split())
matrix = [[0] * (n+1) for i in range(n+1)] #인접행렬
visited = [0] * (n+1)

for i in range(m):
    a,b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1
```

임의의 정점 $v$에 연결된 간선을 모두 찾기 위해 인접행렬의 모든 열을 $V$개 살펴봐야함.

모든 정점에 대해 각 정점별로 연결된 간선을 모두 찾으려면
$O(V^2)$ 시간이 필요

## 인접 리스트 방식

$O(V+E)$

```python
graph = {}
N, M, V = map(int, sys.stdin.readline().split())
for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    if u not in graph:
        graph[u] = list()
    graph[u].append(v)
    if v not in graph:
        graph[v] = list()
    graph[v].append(u)
```

임의의 정점 $v$에 연결된 간선을 모두 찾기 위해 인접행렬의 모든 열을 $E$개 살펴봐야함.

모든 정점에 대해 각 정점별로 연결된 간선을 모두 찾으려면
$O(V+E)$ 시간이 필요
