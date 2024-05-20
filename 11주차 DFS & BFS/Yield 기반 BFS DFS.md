엉둔이의 코드를 기반으로 한 `yield` 문 형식을 활용한 BFS, DFS (제네레이터 generator/이터레이터 iterator)

[제너레이터와 yield 알아보기](https://dojang.io/mod/page/view.php?id=2412)

* 이를통해 로직(알고리즘) 부분과 입출력 부분을 깔끔하게 분리할 수 있다.
* `print()` 문 호출 최소화

```python
from collections import deque
import sys
input = sys.stdin.readline

n,m,v = map(int, input().split())
matrix = [[0] * (n+1) for i in range(n+1)] #인접행렬
visited = [0] * (n+1)

for i in range(m):
    a,b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1

def dfs(v): # p -> [c0 c1, c2]
    visited[v]=1
    yield v # p
    for i in range(1,n+1):
        if (visited[i]==0 and matrix[v][i]==1):
            for u in dfs(i):
                yield u

    #재귀함수 이용 v와 인접한곳 찾고 방문하지 않았다면 다시 dfs

def bfs(v):
    queue = [v]
    visited[v] = 0 #처음에 이거 안돼서
    while queue:
        v = queue.pop(0)
        yield v
        for i in range(1,n+1):
            if(visited[i] == 1 and matrix[v][i] == 1):
                queue.append(i)
                visited[i] = 0


for i in dfs(0):
    print(bin(i))

print(*bfs(v))
```