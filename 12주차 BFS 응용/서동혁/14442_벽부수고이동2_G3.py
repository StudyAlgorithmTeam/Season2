from collections import deque
N, M, K = map(int, input().split())

wall = []
visit = [[[0]*(K + 1) for i in range(M)] for _ in range(N)]
visit[0][0][0] = 1 # 시작점 포함
dx = [1,0,-1,0]
dy = [0,1,0,-1]

for i in range(N):
    wall.append(list(map(int,input())))

def BFS(x, y, count): # 시간복잡도가 어떻게 되는거지?
    queue = deque()
    queue.append((x, y, count))

    while queue:
        x, y, count = queue.popleft()

        if x == N-1 and y == M-1:
            return visit[x][y][count]
        
        for i in range(4):
            dx_x, dy_y = x + dx[i], y + dy[i]

            if dx_x < 0 or dx_x >= N or dy_y < 0 or dy_y >= M:
                continue

            if wall[dx_x][dy_y] == 1 and count < K: # 벽이고 count가 0인 경우
                visit[dx_x][dy_y][count+1] = visit[x][y][count] + 1
                queue.append((dx_x, dy_y, count+1))
                
            elif wall[dx_x][dy_y] == 0 and visit[dx_x][dy_y][count] == 0: # 벽이 아니고 아직 방문하지 않은경우
                visit[dx_x][dy_y][count] = visit[x][y][count] + 1
                queue.append((dx_x,dy_y,count))
            #이미 방문을 한 경우면 그대로 넘어감
    return -1

print(BFS(0,0,0))

'''from collections import deque
q = deque()
from sys import stdin
input = stdin.readline

n,m,k = map(int, input().split())
vis = [[[0]*(k+1) for _ in range(m)] for __ in range(n)]
arr = [list(map(int,input().strip())) for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs() :
    q.append([0,0,k]) # k는 벽을 뚫을 수 있는 수
    vis[0][0][k] = 1
    while q :
        x,y,z = q.popleft()
        if x == n-1 and y == m-1 :
            return vis[x][y][z]
        for i in range(4) :
            nx ,ny = dx[i] + x, dy[i]+y
            if 0<=nx<n and 0<=ny<m :
                if arr[nx][ny]==1 and z>0 and vis[nx][ny][z-1]==0:
                    vis[nx][ny][z-1] = vis[x][y][z]+1
                    q.append([nx,ny,z-1])
                elif arr[nx][ny]==0 and vis[nx][ny][z]==0:
                    vis[nx][ny][z] = vis[x][y][z]+1
                    q.append([nx,ny,z]) 
    return -1

print(bfs()) '''