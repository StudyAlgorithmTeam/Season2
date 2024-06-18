# 준석이의 수학 숙제


import sys


MAX_N = 80000
dp = [0] * (MAX_N+1)
for i in range(3, MAX_N+1):
    dp[i] = dp[i-1]
    if i % 3 == 0 or i % 7 == 0:
        dp[i] += i


if __name__ == "__main__":
    sys.stdin.readline() # T
    for N in map(int, sys.stdin.readline().split()):
        sys.stdout.write(f'{dp[N]}\n')
