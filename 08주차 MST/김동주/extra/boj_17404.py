# RGB거리 2

import enum
import sys


class Color(enum.IntEnum):
    R = 0
    G = 1
    B = 2


N = int(sys.stdin.readline())

# RGB로 칠하는 비용
C = tuple(tuple(map(int, sys.stdin.readline().split())) for i in range(N))

dp = [0, 0, 0]
dp_buffer = [0, 0, 0]

ans = sys.maxsize

for start_color in Color:
    # 초기화
    for color in Color:
        dp[color] = sys.maxsize
    dp[start_color] = C[0][start_color]

    # 답을 구함
    for i in range(1, N):
        dp_buffer[Color.R] = C[i][Color.R] + min(dp[Color.G], dp[Color.B])
        dp_buffer[Color.G] = C[i][Color.G] + min(dp[Color.R], dp[Color.B])
        dp_buffer[Color.B] = C[i][Color.B] + min(dp[Color.R], dp[Color.G])
        dp, dp_buffer = dp_buffer, dp

    # 1번 집의 색상과 N번 집의 색상이 같지 않게끔 처리 (선택 될 수 없게 만듦)
    dp[start_color] = sys.maxsize

    # 최소 비용 갱신
    if min(dp) < ans:
        ans = min(dp)

sys.stdout.write(f'{ans}\n')
