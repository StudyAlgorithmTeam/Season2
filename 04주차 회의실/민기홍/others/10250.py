T = int(input())

result = []

for _ in range(T):
    H, W, N = map(int, input().split())
    floor = N % H
    if N%H == 0:
        result.append(H*100 + N//H)
    else:
        result.append((N%H)*100 + N//H + 1)

for _ in range(T):
    print(result[_])


