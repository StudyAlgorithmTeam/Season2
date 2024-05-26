from collections import deque

N, M = map(int,input().split())

wall = []
visit = [[[0,0] for _ in range(M)] for i in range(N)]
visit[0][0][0] = 1 # 시작점 포함
# N * M * 2 크기의 배열 => 마지막 0,1은 벽을 부순 횟수

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(N):
    wall.append(list(map(int,input())))

def BFS(x, y, count):
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

            if wall[dx_x][dy_y] == 1 and count == 0: # 벽이고 count가 0인 경우
                visit[dx_x][dy_y][1] = visit[x][y][0] + 1
                queue.append((dx_x, dy_y, 1))
                
            elif wall[dx_x][dy_y] == 0 and visit[dx_x][dy_y][count] == 0: # 벽이 아니고 count도 0인 경우
                visit[dx_x][dy_y][count] = visit[x][y][count] + 1
                queue.append((dx_x,dy_y,count))
    return -1

print(BFS(0,0,0))
