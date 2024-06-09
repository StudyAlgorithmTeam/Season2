# binary는 호남선

import sys


def ask_rail(k_th: int) -> int:
    sys.stdout.write(f'? {k_th}\n')
    sys.stdout.flush()
    return int(sys.stdin.readline())


def print_answer(a: int):
    sys.stdout.write(f'! {a}')
    sys.stdout.flush()


if __name__ == "__main__":
    N = int(sys.stdin.readline())

    start = ask_rail(1)
    end = ask_rail(N)

    if start == end:
        a = 0
    elif (end-start) > 0:
        a = 1
    else:
        a = -1

    print_answer(a)
