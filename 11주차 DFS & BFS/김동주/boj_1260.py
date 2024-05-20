import collections
import sys


def solve(n: int, m: int, root: int, graph: dict[int, list[int]]):
    # 방문 순서는 오름차순임을 적용
    for i in graph:
        graph[i].sort()

    # 스택을 이용한 DFS
    visited = [False] * (n+1) # 인덱스에 해당하는 노드를 방문했는지 여부.
    path = [] # 방문 순서대로 노드를 저장할 스택
    stack = [root]
    while stack:
        node = stack.pop()
        if visited[node]:
            continue
        visited[node] = True
        path.append(node)
        for child in reversed(graph[node]):
            if not visited[child]:
                stack.append(child)
    # DFS로 방문한 노드를 방문 순서대로 출력
    print(' '.join(map(str, path)))

    # 큐를 이용한 BFS
    visited = [False] * (n+1) # 인덱스에 해당하는 노드를 방문했는지 여부.
    path = [] # 방문 순서대로 노드를 저장할 스택
    queue = collections.deque([root])
    while queue:
        node = queue.popleft()
        if visited[node]:
            continue
        visited[node] = True
        path.append(node)
        for child in graph[node]:
            if not visited[child]:
                queue.append(child)
    # BFS로 방문한 노드를 방문 순서대로 출력
    print(' '.join(map(str, path)))


if __name__ == "__main__":
    MAX_N = 1000
    MAX_M = 10000
    sys.setrecursionlimit(MAX_N+MAX_M)
    # 표준 입력으로 들어온 데이터 가공
    graph = collections.defaultdict(list)
    N, M, V = map(int, sys.stdin.readline().split())
    for i in range(M):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    # 테스트 케이스 수행
    solve(N, M, V, graph)
