import sys


sudoku = [[0] * 9 for _ in range(9)]
sudoku_fixed = [[False] * 9 for _ in range(9)]


def solve_sudoku(y: int = 0, x: int = 0) -> bool:
    if y >= 9:
        raise StopIteration

    if sudoku_fixed[y][x]:
        solve_sudoku(y+(x+1)//9, (x+1)%9)
    else:
        for num in range(1, 10):
            if validate_cell(y, x, num):
                sudoku[y][x] = num
                solve_sudoku(y+(x+1)//9, (x+1)%9)
                sudoku[y][x] = 0


def validate_cell(y: int, x: int, num: int) -> bool:
    return validate_row_of(x, y, num) and validate_column_of(x, y, num) and validate_subgrid_of(y, x, num)


def validate_row_of(x: int, y: int, num: int) -> bool:
    for x in range(9):
        if sudoku[y][x] == num:
            return False
    return True


def validate_column_of(x: int, y: int, num: int) -> bool:
    for y in range(9):
        if sudoku[y][x] == num:
            return False
    return True


def validate_subgrid_of(y: int, x: int, num: int) -> bool:
    sy = 3 * (y // 3)
    sx = 3 * (x // 3)
    for y in range(sy, sy+3):
        for x in range(sx, sx+3):
            if sudoku[y][x] == num:
                return False
    return True


if __name__ == "__main__":
    # 입력 받는다
    for y in range(9):
        for x, num in enumerate(map(int, sys.stdin.readline().strip())):
            sudoku[y][x] = num
            sudoku_fixed[y][x] = num != 0

    # 푼다
    try:
        solve_sudoku()
    except StopIteration:
        pass

    # 출력 한다
    for y in range(9):
        for x in range(9):
            sys.stdout.write(str(sudoku[y][x]))
        sys.stdout.write('\n')
