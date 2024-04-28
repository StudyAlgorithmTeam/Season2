# 2048 (Easy)

import enum
import sys


N: int


class Direction(enum.IntEnum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3


class Grid:
    def __init__(self, n) -> None:
        self.grid = [[0] * N for y in range(N)]
        self.n  = n

    def __getitem__(self, index):
        return self.grid[index]

    def max(self):
        ret = 0
        for y in range(self.n):
            for x in range(self.n):
                if ret < self[y][x]:
                    ret = self[y][x]
        return ret

    def copy(self, src_grid):
        for y in range(self.n):
            for x in range(self.n):
                self[y][x] = src_grid[y][x]

    def swipe(self, direction):
        if direction == Direction.LEFT:
            for y in range(self.n):
                src_x, dst_x = 0, 0
                while src_x < self.n:
                    if self[y][src_x] == 0 or src_x == dst_x:
                        # 채울 숫자가 없다면 건너 뛰기
                        src_x += 1
                    elif self[y][dst_x] == 0:
                        # 빈 칸에 채워넣기
                        self[y][dst_x] = self[y][src_x]
                        self[y][src_x] = 0
                        src_x += 1
                    elif self[y][dst_x] == self[y][src_x]:
                        # 같은 두 숫자 합치기
                        self[y][dst_x] += self[y][src_x]
                        self[y][src_x] = 0
                        src_x += 1
                        dst_x += 1
                    else:
                        #서로 다른 숫자면 다음 칸에 채워넣기
                        dst_x += 1
        elif direction == Direction.RIGHT:
            for y in range(self.n):
                src_x, dst_x = self.n-1, self.n-1
                while src_x >= 0:
                    if self[y][src_x] == 0 or src_x == dst_x:
                        # 채울 숫자가 없다면 건너 뛰기
                        src_x -= 1
                    elif self[y][dst_x] == 0:
                        # 빈 칸에 채워넣기
                        self[y][dst_x] = self[y][src_x]
                        self[y][src_x] = 0
                        src_x -= 1
                    elif self[y][dst_x] == self[y][src_x]:
                        # 같은 두 숫자 합치기
                        self[y][dst_x] += self[y][src_x]
                        self[y][src_x] = 0
                        src_x -= 1
                        dst_x -= 1
                    else:
                        #서로 다른 숫자면 다음 칸에 채워넣기
                        dst_x -= 1
        elif direction == Direction.DOWN:
            for x in range(self.n):
                src_y, dst_y = 0, 0
                while src_y < self.n:
                    if self[src_y][x] == 0 or src_y == dst_y:
                        # 채울 숫자가 없다면 건너 뛰기
                        src_y += 1
                    elif self[dst_y][x] == 0:
                        # 빈 칸에 채워넣기
                        self[dst_y][x] = self[src_y][x]
                        self[src_y][x] = 0
                        src_y += 1
                    elif self[dst_y][x] == self[src_y][x]:
                        # 같은 두 숫자 합치기
                        self[dst_y][x] += self[src_y][x]
                        self[src_y][x] = 0
                        src_y += 1
                        dst_y += 1
                    else:
                        #서로 다른 숫자면 다음 칸에 채워넣기
                        dst_y += 1
        elif direction == Direction.UP:
            for x in range(self.n):
                src_y, dst_y = self.n-1, self.n-1
                while src_y >= 0:
                    if self[src_y][x] == 0 or src_y == dst_y:
                        # 채울 숫자가 없다면 건너 뛰기
                        src_y -= 1
                    elif self[dst_y][x] == 0:
                        # 빈 칸에 채워넣기
                        self[dst_y][x] = self[src_y][x]
                        self[src_y][x] = 0
                        src_y -= 1
                    elif self[dst_y][x] == self[src_y][x]:
                        # 같은 두 숫자 합치기
                        self[dst_y][x] += self[src_y][x]
                        self[src_y][x] = 0
                        src_y -= 1
                        dst_y -= 1
                    else:
                        #서로 다른 숫자면 다음 칸에 채워넣기
                        dst_y -= 1



if __name__ == "__main__":
    N = int(sys.stdin.readline())

    grid_snapshots = [ Grid(N) for move in range(6) ]


    # make initial state
    initial_state = grid_snapshots[0]
    for y in range(N):
        for x, num in enumerate(map(int, sys.stdin.readline().split())):
            initial_state[y][x] = num


    def backtrack(moves):
        curr_grid = grid_snapshots[moves]
        if moves == 5:
            yield curr_grid.max()
        else:
            next_grid = grid_snapshots[moves+1]
            for direction in Direction:
                next_grid.copy(curr_grid)
                next_grid.swipe(direction)
                yield max(backtrack(moves+1))

    sys.stdout.write(max(backtrack(0)).__str__())
