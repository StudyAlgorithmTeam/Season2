from sys import stdin


N = 10
INF = 1000
RAW_BULB_ON = 'O'

raw_grid = stdin.readlines()

# bitmasked grid
grid = [0] * N

KERNEL = [
    (0b111) << 8,
    (0b010) << 8,
    (0b010) << 8, # 음수 인덱싱 고려하여 아래로 배치
]


def press_switch(y: int, x: int):
    for dy in (-1, 0, 1):
        if (y+dy) < 0 or (y+dy) >= N:
            continue
        grid[y+dy] ^= (KERNEL[dy] >> x) & 0b1111111111


def backtrack(y: int = 0, x: int = 0):
    # 모든 전구가 다 꺼짐
    if sum(grid) == 0:
        return 0

    # 모든 라인을 다 검사 했지만, 완성 X
    if y >= N:
        return INF

    # 다음 라인도 검사
    if x >= N:
        return backtrack(y+1, 0)

    # 컨셉은, 지금 보고 있는 좌표의 이전 행 전체와,
    # 같은 행의 이전 열들을 반복하여 수정하지 않는 것.

    ans = INF

    if grid[y] & (0b1000000000 >> x) == 0:
        # 불이 꺼져있으므로 아무것도 하지 않아본다.
        return backtrack(y, x+1)

    if ans != 0 and y == 0 and x == 0:
        # 나 자신을 끔
        press_switch(y, x)
        ans = min(backtrack(y, x+1)+1, ans)
        press_switch(y, x)
    if ans != 0 and y == 0 and x < (N-1):
        # 나를 끄기 위해 오른쪽 것을 끔
        press_switch(y, x+1)
        ans = min(backtrack(y, x+1)+1, ans)
        press_switch(y, x+1)
    if ans != 0 and y < (N-1) :
        # 나를 끄기 위해 아래에 있는 것을 끔
        press_switch(y+1, x)
        ans = min(backtrack(y, x+1)+1, ans)
        press_switch(y+1, x)
    return ans


def render():
    """디버그용 함수"""
    lines = []
    for y in range(N):
        lines.append(f'{grid[y] % (1 << 10):010b}')
    return lines


if __name__ == '__main__':
    for y in range(N):
        for x in range(N):
            grid[y] <<= 1
            if raw_grid[y][x] == RAW_BULB_ON:
                grid[y] |= 1
    ans = backtrack()
    if ans == INF:
        print(-1)
    else:
        print(ans)
