N = int(input())
E = int(input())

graph = [[] for i in range(N+1)]
visit = [0] * (N+1)
visit[1] = 1
count = 0

for i in range(E):
    s, e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

def dfs(x):
    global count

    for i in graph[x]:
        if visit[i] == 0:
            visit[i] = 1
            count = count + 1
            dfs(i)
dfs(1)

print(count)

# 1 => 2 ,5
# 2 => 1, 3, 5
# 3 => 2
# 4 => 7
# 5 => 1, 2, 6