# 제곱수 찾기

import math
import sys


N, M = map(int, sys.stdin.readline().split())
A = sys.stdin.readlines()


def make_numbers(y: int, x: int, y_step: int, x_step: int):
    number = ''
    if y_step == x_step == 0:
        number += A[y][x]
        yield int(number)
    else:
        while 0 <= y < N and 0 <= x < M:
            number += A[y][x]
            yield int(number)
            y += y_step
            x += x_step


def is_complete_square(x: int) -> bool:
    # 완전 제곱수인가?
    root = math.sqrt(x)
    return root == int(root)


def find_complete_square_numbers():
    for y_step in range(-N, N):
        for x_step in range(-M, M):
            for y in range(N):
                for x in range(M):
                    for num in make_numbers(y, x, y_step, x_step):
                        if is_complete_square(num):
                             yield num


print(
    max(find_complete_square_numbers(), default=-1)
)
