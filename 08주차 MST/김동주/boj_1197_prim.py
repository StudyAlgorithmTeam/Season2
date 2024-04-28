from typing import *
import heapq
import sys


if __name__ == "__main__":
    V, E = map(int, sys.stdin.readline().split())

    graph = {}
    for i in range(E):
        u, v, w = map(int, sys.stdin.readline().split())
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append((w, v))
        graph[v].append((w, u))


    visited = [False] * (V+1)
    pq = [(0, 1)]
    total_w = 0

    while pq:
        w, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        total_w += w
        for w, v in graph[u]:
            if not visited[v]:
                heapq.heappush(pq, (w, v))

    sys.stdout.write(f"{total_w}\n")
