from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
maps = [list(map(int, list(input().rstrip()))) for _ in range(n)]
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
visited[0][0][0]=1

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y,z):
    q = deque()
    q.append((x,y,z))
    while q:
        x,y,c = q.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][c]
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0 <= xx < n and 0 <= yy < m:
                if maps[xx][yy]==1 and c==0:
                    visited[xx][yy][c+1]=visited[x][y][c]+1
                    q.append((xx,yy,c+1))
                elif maps[xx][yy] == 0:
                    visited[xx][yy][c] = visited[x][y][c]+1
                    q.append((xx,yy,c))
          #죄성함다..
    return -1

print(bfs(0,0,0))
