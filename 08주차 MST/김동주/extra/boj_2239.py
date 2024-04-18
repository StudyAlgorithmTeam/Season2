import sys


sudoku = [[0] * 9 for _ in range(9)]
sudoku_fixed = [[False] * 9 for _ in range(9)]

row_hint = [set(range(1,10)) for _ in range(9)]
column_hint = [set(range(1,10)) for _ in range(9)]
subgrid_hint = [[set(range(1,10)) for _ in range(3)] for _ in range(3)]


def solve_next_cell(y: int = 0, x: int = 0) -> bool:
    if y >= 9:
        raise StopIteration

    # 다음에 풀 스도쿠 좌표
    ny, nx = y+(x+1)//9, (x+1)%9

    if sudoku_fixed[y][x]:
        solve_next_cell(ny, nx)
    else:
        for num in range(1, 10):
            if validate_cell(y, x, num):
                fill_cell(y, x, num)
                solve_next_cell(ny, nx)
                unfill_cell(y, x, num)


def validate_cell(y: int, x: int, num: int) -> bool:
    return validate_row_of(x, y, num) and validate_column_of(x, y, num) and validate_subgrid_of(y, x, num)


def validate_row_of(x: int, y: int, num: int) -> bool:
    return num in row_hint[y]


def validate_column_of(x: int, y: int, num: int) -> bool:
    return num in column_hint[x]


def validate_subgrid_of(y: int, x: int, num: int) -> bool:
    return num in subgrid_hint[y//3][x//3]


def fill_cell(y: int, x: int, num: int):
    sudoku[y][x] = num
    row_hint[y].remove(num)
    column_hint[x].remove(num)
    subgrid_hint[y//3][x//3].remove(num)


def unfill_cell(y: int, x: int, num: int):
    sudoku[y][x] = 0
    row_hint[y].add(num)
    column_hint[x].add(num)
    subgrid_hint[y//3][x//3].add(num)


if __name__ == "__main__":
    # 입력 받는다
    for y in range(9):
        for x, num in enumerate(map(int, sys.stdin.readline().strip())):
            if num != 0:
                fill_cell(y, x, num)
                sudoku_fixed[y][x] = True

    # 푼다
    try:
        solve_next_cell()
    except StopIteration:
        pass

    # 출력 한다
    for y in range(9):
        for x in range(9):
            sys.stdout.write(str(sudoku[y][x]))
        sys.stdout.write('\n')
