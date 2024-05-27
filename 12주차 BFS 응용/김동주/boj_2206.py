import collections
import sys


MAX_N = 1000
MAX_M = 1000
WALL = '1'


N, M = map(int, sys.stdin.readline().split())
mat = sys.stdin.readlines()
visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]
q = collections.deque([(0,0,True)])
width = 0
depth = 0
while q:
    if width == 0:
        width = len(q)
        depth += 1
    y, x, breakable = q.popleft()
    width -= 1
    if (y < 0 or x < 0 or y >= N or x >= M) or visited[y][x][breakable]:
        continue
    visited[y][x][breakable] = True
    if mat[y][x] == WALL:
        if not breakable:
            continue
        breakable = False
    q.append((y+1, x, breakable))
    q.append((y, x+1, breakable))
    q.append((y, x-1, breakable))
    q.append((y-1, x, breakable))
    if y == (N-1) and x == (M-1):
        print(depth)
        break
else:
    print("-1")
