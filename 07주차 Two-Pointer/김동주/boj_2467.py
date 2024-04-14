N = int(input())
liquid = sorted(map(int, input().split()), key=abs)

min_res = int(1e10)
min_values = [0, 0]

for i in range(N-1):
    res = abs(liquid[i]+liquid[i+1])
    if min_res > res:
        min_res = res
        min_values[:] = liquid[i], liquid[i+1]

print(*sorted(min_values))
