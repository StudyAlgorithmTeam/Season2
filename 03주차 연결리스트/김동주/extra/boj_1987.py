from sys import stdin
from sys import stdout


R, C = map(int, stdin.readline().split())

grid = stdin.readlines()
visited = { c: False for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}


def backtrack(r: int, c: int):
    if r < 0 or R <= r or c < 0 or C <= c or visited[grid[r][c]]:
        return 0
    visited[grid[r][c]] = True
    ans = 1 + max(
        backtrack(r-1, c),
        backtrack(r, c-1),
        backtrack(r+1, c),
        backtrack(r, c+1),
    )
    visited[grid[r][c]] = False
    return ans


stdout.write(backtrack(0, 0).__str__() + '\n')
