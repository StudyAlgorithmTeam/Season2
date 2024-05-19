N, M, K = map(int, input().split())

block = [[0]*(M+1) for i in range(N+1)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

for i in range(1,N+1):
    tmp = input()
    for j in range(M):
        if tmp[j] == "1":
            block[i][j+1] = 1


