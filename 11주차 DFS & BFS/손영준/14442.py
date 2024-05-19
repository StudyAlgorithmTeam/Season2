from collections import deque
import sys
input = sys.stdin.readline

n,m,k = map(int, input().split())
maps = [list(map(int, list(input().rstrip()))) for _ in range(n)]
visited = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]
visited[0][0][0]=1

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs():
    q = deque()
    q.append((0,0,0,1))
    while q:
        
