from collections import deque
from sys import stdin
input = stdin.readline
N, M, K = map(int, input().split())

wall = []
visit = [[[0]*(K + 1) for i in range(M)] for _ in range(N)]
visit[0][0][0] = 1 # 시작점 포함

dx = [1,0,-1,0]
dy = [0,1,0,-1]

for i in range(N):
    wall.append(list(map(int,input().strip())))

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

            if wall[dx_x][dy_y] == 1 and count < K and visit[dx_x][dy_y][count+1] == 0:
                visit[dx_x][dy_y][count+1] = visit[x][y][count] + 1
                queue.append((dx_x, dy_y, count+1))
                
            elif wall[dx_x][dy_y] == 0 and visit[dx_x][dy_y][count] == 0: # 벽이 아니고 아직 방문하지 않은경우
                visit[dx_x][dy_y][count] = visit[x][y][count] + 1
                queue.append((dx_x,dy_y,count))
            #이미 방문을 한 경우면 그대로 넘어감
    return -1

print(BFS(0,0,0))