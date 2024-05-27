import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
map_arr = []

# 미로를 저장하는 배열
for i in range(N):
    map_arr.append(list(map(int, input().rstrip())))

# 상하 좌우 이동을 담당
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, K):
    # 벽을 몇 번 부수고 도달했는지에 대한 3차원 배열 좌표당 K+1개가 있음
    visited = [[[False] * (K + 1) for _ in range(M)] for _ in range(N)]
    
    queue = deque()
    queue.append((x, y, 0))
    
    visited[x][y][0] = True
    
    # distance는 거리를 저장하는 배열, 각 위치마다 도달하는데 얼마나 걸리는지
    distance = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]
    distance[x][y][0] = 1
    
    while queue:
        x, y, k = queue.popleft()
        
        # 목적지에 도달한 경우
        if x == N - 1 and y == M - 1:
            return distance[x][y][k]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # BFS의 기본적인 조건문
            if 0 <= nx < N and 0 <= ny < M:
                # 이동을 했는데 벽을 부수지 않는 경우
                if map_arr[nx][ny] == 0 and not visited[nx][ny][k]:
                    queue.append((nx, ny, k))
                    visited[nx][ny][k] = True
                    distance[nx][ny][k] = distance[x][y][k] + 1
                # 이동은 했는데 벽을 부수는 경우
                elif map_arr[nx][ny] == 1 and k < K and not visited[nx][ny][k + 1]:
                    #k가 하나 증가 했기 때문에 k+1
                    queue.append((nx, ny, k + 1))
                    visited[nx][ny][k + 1] = True
                    distance[nx][ny][k + 1] = distance[x][y][k] + 1
    
    return -1
    #끝에 도달하지 못하면  -1 출력

print(bfs(0, 0, K))
