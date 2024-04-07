import sys
import typing


R: int
C: int
T: int
grid: typing.List[typing.List[int]]
air_cleaner_rows: typing.List[int]


def simulate(seconds: int):
    for _ in range(seconds):
        diffuse()
        ventilate()

def diffuse():
    """O(RC)"""
    after = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            after[r][c] += grid[r][c]
            if grid[r][c] > 0:
                diff = grid[r][c] // 5
                for cr, cc in _diffusable_coords(r, c):
                    after[cr][cc] += diff
                    after[r][c] -= diff
    for r in range(R):
        for c in range(C):
            grid[r][c] = after[r][c]

def ventilate():
    """O(R+C)"""
    min_c = 0
    max_c = C-1
    # 반시계 방향
    min_r = 0
    max_r = air_cleaner_rows[0]
    for r in range(max_r-1, min_r, -1):
        grid[r][min_c] = grid[r-1][min_c]
    for c in range(min_c, max_c):
        grid[min_r][c] = grid[min_r][c+1]
    for r in range(min_r, max_r):
        grid[r][max_c] = grid[r+1][max_c]
    for c in range(max_c, min_c, -1):
        grid[max_r][c] = grid[max_r][c-1]
    grid[max_r][min_c+1] = 0 # 깨끗한 공기
    # 시계방향
    min_r = air_cleaner_rows[1]
    max_r = R-1
    for r in range(min_r+1, max_r):
        grid[r][min_c] = grid[r+1][min_c]
    for c in range(min_c, max_c):
        grid[max_r][c] = grid[max_r][c+1]
    for r in range(max_r, min_r, -1):
        grid[r][max_c] = grid[r-1][max_c]
    for c in range(max_c, min_c+1, -1):
        grid[min_r][c] = grid[min_r][c-1]
    grid[min_r][min_c+1] = 0 # 깨끗한 공기

def _diffusable_coords(r: int, c: int) -> typing.Iterable[typing.Tuple[int, int]]:
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nr, nc = r+dr, c+dc
        if _is_bound(nr, nc) and not _is_air_clearner(nr, nc):
            yield nr, nc

def _is_bound(r: int, c: int) -> bool:
    return r >= 0 and c >= 0 and r < R and c < C

def _is_air_clearner(r: int, c: int) -> bool:
    return grid[r][c] == -1


if __name__ == '__main__':
    R, C, T = map(int, sys.stdin.readline().split())
    grid = [[None] * C for _ in range(R)]
    air_cleaner_rows = []

    for r, line in enumerate(sys.stdin.readlines()):
        for c, cell in enumerate(map(int, line.strip().split())):
            grid[r][c] = cell
            if cell == -1:
                air_cleaner_rows.append(r)

    simulate(T)
    answer = sum(sum(grid[r]) for r in range(R)) + 2 # 뒤에 2는 공기청정기 2대 땜에 -1 두번 된 것 보정.
    sys.stdout.write(f'{answer}\n')
