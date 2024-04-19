import sys
import typing


class Sudoku:
    def __init__(self) -> None:
        self.grid = [[0]*9 for _ in range(9)]
        self.fixed = [[False]*9 for _ in range(9)]

    def print(self):
        for y in range(9):
            for x in range(9):
                sys.stdout.write(f'{self.grid[y][x]} ')
            sys.stdout.write('\n')

    def fill(self, y: int, x: int, num: int, fixed: bool=False):
        self.grid[y][x] = num
        self.fixed[y][x] = fixed

    def unfill(self, y: int, x: int):
        self.grid[y][x] = 0

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
            return
        for num in range(1, 10):
            if not self._validate(y, x, num):
                continue
            self.fill(y, x, num)
            self._solve_util(ny, nx)
            self.unfill(y, x)
        return

    def _validate(self, y: int, x: int, num: int) -> bool:
        if num in self._row_iterator(y):
            return False
        if num in self._column_iterator(x):
            return False
        if num in self._subgrid_iterator(y, x):
            return False
        return True

    def _row_iterator(self, y: int) -> typing.Iterator[int]:
        for x in range(9):
            yield self.grid[y][x]

    def _column_iterator(self, x: int) -> typing.Iterator[int]:
        for y in range(9):
            yield self.grid[y][x]

    def _subgrid_iterator(self, y: int, x: int) -> typing.Iterator[int]:
        sg_y = y//3
        sg_x = x//3
        for y in range(3*sg_y, 3*sg_y+3):
            for x in range(3*sg_x, 3*sg_x+3):
                yield self.grid[y][x]


if __name__ == "__main__":
    sudoku = Sudoku()

    for y in range(9):
        for x, num in enumerate(map(int, sys.stdin.readline().split())):
            if num != 0:
                sudoku.fill(y, x, num, fixed=True)

    sudoku.solve()
    sudoku.print()
