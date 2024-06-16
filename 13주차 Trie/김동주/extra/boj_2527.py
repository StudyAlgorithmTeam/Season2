# 직사각형


def is_type_d(x1, y1, p1, q1, x2, y2, p2, q2):
    return bool(
        x1 > p2 or
        x2 > p1 or
        y1 > q2 or
        y2 > q1
    )


def is_type_c(x1, y1, p1, q1, x2, y2, p2, q2):
    return bool(
        (x1 == p2 and y1 == q2) or
        (p1 == x2 and q1 == y2) or
        (x1 == p2 and q1 == y2) or
        (p1 == x2 and y1 == q2)
    )


def is_type_b(x1, y1, p1, q1, x2, y2, p2, q2):
    return bool(
        x1 == p2 or
        x2 == p1 or
        y1 == q2 or
        y2 == q1
    )


for t in range(4):
    x = tuple(map(int, input().split()))
    if is_type_d(*x):
        print('d')
    elif is_type_c(*x):
        print('c')
    elif is_type_b(*x):
        print('b')
    else:
        print('a')
