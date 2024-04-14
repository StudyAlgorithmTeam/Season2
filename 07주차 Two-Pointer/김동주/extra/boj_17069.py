import sys


def testcase(tid):
    N = int(sys.stdin.readline())
    grid = [[*map(int, sys.stdin.readline().split())] for _ in range(N)]
    dp = [[[0]*3 for _ in range(N)] for _ in range(N)]
    # dp[y][x][i] : 파이프의 가장 오른쪽 아래가 (x, y)좌표일 때, 파이프의 상태가 i(0: 가로, 1: 대각선, 2: 세로)인 경우의 수

    dp[0][1][0] = 1
    for y in range(N):
        for x in range(N):
            # 파이프의 오른쪽 아래 끝을 (x,y)로 옮겨볼 거에요.
            if grid[y][x] == 1:
                continue

            # 아래는 문제에서 제시하는 파이프를 밀 수 있는 모든 경우의 수들이다.

            # 가로
            if x > 0:
                dp[y][x][0] += dp[y][x-1][0]
            if x > 0 and y > 0 and grid[y-1][x] == 0 and grid[y][x-1] == 0:
                dp[y][x][1] += dp[y-1][x-1][0]

            # 세로
            if y > 0:
                dp[y][x][2] += dp[y-1][x][2]
            if x > 0 and y > 0 and grid[y-1][x] == 0 and grid[y][x-1] == 0:
                dp[y][x][1] += dp[y-1][x-1][2]

            # 대각선
            if x > 0:
                dp[y][x][0] += dp[y][x-1][1]
            if y > 0:
                dp[y][x][2] += dp[y-1][x][1]
            if x > 0 and y > 0 and grid[y-1][x] == 0 and grid[y][x-1] == 0:
                dp[y][x][1] += dp[y-1][x-1][1]

    sys.stdout.write(f'{sum(dp[N-1][N-1])}\n')


if __name__ == '__main__':
    # sys.setrecursionlimit(int(1e6))
    # T = int(sys.stdin.readline())
    # for tid in range(1, T+1):
    #     testcase(tid)
    testcase(0)
