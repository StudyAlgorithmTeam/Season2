import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = []

for _ in range(N):
    board.append(input().strip())

def changing_color(bit):
    if bit == True:
        color = 'B'
    else:
        color = 'W'
    return not bit, color

# 첫 사각형을 W로 바꾸는 경우
def To_W(board, n, m):
    count = 0
    for i in range(8):
        if i%2 == 0:
            bit, color = changing_color(False)
        else:
            bit, color = changing_color(True)
        for j in range(8):
            if board[i+n][j+m] != color:
                count += 1
            bit, color = changing_color(bit)

    return count

# 첫 사각형을 B로 바꾸는 경우
def To_B(board, n, m):
    count = 0
    for i in range(8):
        if i%2 == 0:
            bit, color = changing_color(True)
        else:
            bit, color = changing_color(False)
        for j in range(8):
            if board[i+n][j+m] != color:
                count += 1
            bit, color = changing_color(bit)

    return count

# 브루트포스(전수조사)
# 아이디어: 8x8 범위를 계속 조사
minimum = 32 # 최대값이 32

for i in range(N-7):
    for j in range(M-7):
        minimum = min(To_W(board, i, j), To_B(board, i, j), minimum)

print(minimum)


