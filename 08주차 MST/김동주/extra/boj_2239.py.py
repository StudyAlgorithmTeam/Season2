import sys


class Sudoku:
    def __init__(self) -> None:
        self.grid = [[0]*9 for _ in range(9)]
        self.fixed = [[False]*9 for _ in range(9)]
        self.row_flag = [0] * 9
        self.col_flag = [0] * 9
        self.sgr_flag = [[0]*3 for _ in range(3)]

    def print(self):
        for y in range(9):
            for x in range(9):
                sys.stdout.write(f'{self.grid[y][x]}')
            sys.stdout.write('\n')

    def fill(self, y: int, x: int, num: int, fixed: bool=False):
        self.grid[y][x] = num
        self.fixed[y][x] = fixed
        flag = 1 << num
        self.row_flag[y] |= flag
        self.col_flag[x] |= flag
        self.sgr_flag[y//3][x//3] |= flag

    def unfill(self, y: int, x: int):
        num = self.grid[y][x]
        self.grid[y][x] = 0
        flag = 1 << num
        self.row_flag[y] &= ~flag
        self.col_flag[x] &= ~flag
        self.sgr_flag[y//3][x//3] &= ~flag

    def solve(self):
        try:
            self._solve_util(0, 0)
        except StopIteration:
            pass

    def _solve_util(self, y: int, x: int):
        if y >= 9:
            raise StopIteration
        ny, nx = y+(x+1)//9, (x+1)%9 # 다음에 풀 스도쿠 좌표
        if self.fixed[y][x]:
            self._solve_util(ny, nx)
        else:
            for num in self._possible_numbers(y, x):
                self.fill(y, x, num)
                self._solve_util(ny, nx)
                self.unfill(y, x)
        return

    def _possible_numbers(self, y: int, x: int):
        flags = self.row_flag[y] | self.col_flag[x] | self.sgr_flag[y//3][x//3]
        for num in range(1, 10):
            flags >>= 1
            if (flags & 1) == 0:
                yield num


if __name__ == "__main__":
    sudoku = Sudoku()

    for y in range(9):
        for x, num in enumerate(map(int, sys.stdin.readline().strip())):
            if num != 0:
                sudoku.fill(y, x, num, fixed=True)

    sudoku.solve()
    sudoku.print()
