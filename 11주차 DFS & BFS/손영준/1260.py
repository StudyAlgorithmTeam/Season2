from collections import deque
import sys
input = sys.stdin.readline

n,m,v = map(int, input().split())
matrix = [[0] * (n+1) for i in range(n+1)] #인접행렬
visited = [0] * (n+1)

for i in range(m):
    a,b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1
    
def dfs(v):
    visited[v]=1
    print(v, end=' ')
    for i in range(1,n+1):
        if (visited[i]==0 and matrix[v][i]==1):
            dfs(i)
    #재귀함수 이용 v와 인접한곳 찾고 방문하지 않았다면 다시 dfs

def bfs(v):
    queue = [v]
    visited[v] = 0 #처음에 이거 안돼서
    
    while queue:
        v = queue.pop(0)
        print(v, end=' ')
        for i in range(1,n+1):
            if(visited[i] == 1 and matrix[v][i] == 1):
                queue.append(i)
                visited[i] = 0
                
dfs(v)
print()
bfs(v)
                
    
