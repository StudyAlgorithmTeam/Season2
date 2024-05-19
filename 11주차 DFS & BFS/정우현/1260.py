N, M, V = map(int, input().split())
G = [[0]*(N+1) for _ in range(N+1)]
#리스트- 컴프리헨션
#[0,0,0,0]인 배열을 N+1개 만든다
#N+1로 하는 이유 -> 3을 하면 0123 으로 되는데 입력은 1,2로 받으니까
#정학한 위치에 가려면 1을 더해서 사용해야 한다 0은 안쓴다
for i in range(M):
    a, b = map(int, input().split())
    G[a][b] = G[b][a] = 1

dfsarr = [0]*(N+1)
bfsarr = dfsarr.copy()

def dfs(V):
    dfsarr[V] = 1
    print(V, end = " ")
    for i in range(1, N+1):
    #0은 볼 필요 없으니까 1부터 확인한다
        if (dfsarr[i] == 0 and G[V][i] == 1):
        #첫번째 조건은 방문한 적이 있는지 두번째는 값이 존재하는지
            dfs(i)

def bfs(V):
    queue = [V]
    bfsarr[V] = 1
    while queue:
        V = queue.pop(0)
        print(V, end = " ")
        for i in range(1, N+1):
            if (bfsarr[i] == 0 and G[V][i] == 1):
                queue.append(i)
                #여기서 i를 빼주는건 연결된 값이 (1,2)면 1번째 열 2번째 행에
                #위치하기 때문에
                bfsarr[i] = 1

dfs(V)
print()
bfs(V)
