from collections import defaultdict
from collections import deque
from heapq import heappush
from heapq import heappop
from sys import stdin
from sys import stdout


def testcase(tid):
    V, E = map(int, stdin.readline().split())

    graph = defaultdict(list)
    visited = [False] * (V+1)
    verticies = deque(range(1, V+1))
    answer = 0

    for i in range(E):
        A, B, C = map(int, stdin.readline().split())
        heappush(graph[A], (C, B))
        heappush(graph[B], (C, A))

    while verticies:
        u = verticies.popleft()
        if not visited[u]:
            w, v = heappop(graph[u])
            answer += w
            visited[u] = True
            visited[v] = True

    stdout.write(str(answer))
    stdout.write('\n')


if __name__ == '__main__':
    # T = int(stdin.readline())
    # for tid in range(1, T+1):
    #     testcase(tid)
    testcase(0)
