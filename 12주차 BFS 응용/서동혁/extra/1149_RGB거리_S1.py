N = int(input())

color_cost = [[0,0,0]]

for i in range(N):
    color_cost.append(list(map(int,input().split())))

for i in range(1,N+1):
    color_cost[i][0] = min(color_cost[i-1][1],color_cost[i-1][2]) + color_cost[i][0]
    color_cost[i][1] = min(color_cost[i-1][0],color_cost[i-1][2]) + color_cost[i][1]
    color_cost[i][2] = min(color_cost[i-1][0],color_cost[i-1][1]) + color_cost[i][2]

print(min(color_cost[N]))