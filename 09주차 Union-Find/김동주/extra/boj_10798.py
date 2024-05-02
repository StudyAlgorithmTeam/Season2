import sys

grid = list(map(lambda s:s.strip(), sys.stdin.readlines()))
h = len(grid)
max_w = max(map(len,grid))

for x in range(max_w):
    for y in range(h):
        if x < len(grid[y]):
            sys.stdout.write(grid[y][x])