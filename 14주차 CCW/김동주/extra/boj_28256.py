# 초콜릿 보관함

from typing import *
import sys


graph = {
    (0, 0): ((0, 1), (1, 0), ),
    (0, 1): ((0, 0), (0, 2), ),
    (0, 2): ((0, 1), (1, 2), ),
    (1, 0): ((0, 0), (2, 0), ),
    (1, 2): ((0, 2), (2, 2), ),
    (2, 0): ((2, 1), (1, 0), ),
    (2, 1): ((2, 0), (2, 2), ),
    (2, 2): ((2, 1), (1, 2), ),
}


def count(grid: List[List[str]], y: int, x: int) -> int:
    cnt = 1
    grid[y][x] = 'X'
    for cy, cx in graph[y, x]:
        if grid[cy][cx] == 'O':
            cnt += count(grid, cy, cx)
    return cnt


def is_scr_valid(grid: List[List[str]], n: int, a: Tuple[int]) -> bool:
    a_hat = []
    for y, x in graph:
        if grid[y][x] == 'O':
            a_hat.append(count(grid, y, x))
    if len(a_hat) != n:
        return False
    a_hat.sort()
    for i in range(n):
        if a_hat[i] != a[i]:
            return False
    return True


if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for t in range(T):
        grid = [
            list(sys.stdin.readline().strip()),
            list(sys.stdin.readline().strip()),
            list(sys.stdin.readline().strip()),
        ]
        n, *a = map(int, sys.stdin.readline().split())
        if is_scr_valid(grid, n, a):
            sys.stdout.write('1\n')
        else:
            sys.stdout.write('0\n')
